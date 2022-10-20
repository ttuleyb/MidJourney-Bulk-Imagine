import time
import struct

import Quartz.CoreGraphics as CG

class ScreenPixel(object):
    """Captures the screen using CoreGraphics, and provides access to
    the pixel values.
    """

    def capture(self, region = None):
        """region should be a CGRect, something like:

        >>> import Quartz.CoreGraphics as CG
        >>> region = CG.CGRectMake(0, 0, 100, 100)
        >>> sp = ScreenPixel()
        >>> sp.capture(region=region)

        The default region is CG.CGRectInfinite (captures the full screen)
        """

        if region is None:
            region = CG.CGRectInfinite
        else:
            # TODO: Odd widths cause the image to warp. This is likely
            # caused by offset calculation in ScreenPixel.pixel, and
            # could could modified to allow odd-widths
            if region.size.width % 2 > 0:
                emsg = "Capture region width should be even (was %s)" % (
                    region.size.width)
                raise ValueError(emsg)

        # Create screenshot as CGImage
        image = CG.CGWindowListCreateImage(
            region,
            CG.kCGWindowListOptionOnScreenOnly,
            CG.kCGNullWindowID,
            CG.kCGWindowImageDefault)

        # Intermediate step, get pixel data as CGDataProvider
        prov = CG.CGImageGetDataProvider(image)

        # Copy data out of CGDataProvider, becomes string of bytes
        self._data = CG.CGDataProviderCopyData(prov)

        # Get width/height of image
        self.width = CG.CGImageGetWidth(image)
        self.height = CG.CGImageGetHeight(image)

    def pixel(self, x, y):
        """Get pixel value at given (x,y) screen coordinates

        Must call capture first.
        """

        # Pixel data is unsigned char (8bit unsigned integer),
        # and there are for (blue,green,red,alpha)
        data_format = "BBBB"

        # Calculate offset, based on
        # http://www.markj.net/iphone-uiimage-pixel-color/
        offset = 4 * ((self.width*int(round(y))) + int(round(x)))

        # Unpack data from string into Python'y integers
        b, g, r, a = struct.unpack_from(data_format, self._data, offset=offset)

        # Return BGRA as RGBA
        return (r, g, b, a)


if __name__ == '__main__':
    # Timer helper-function
    import contextlib

    @contextlib.contextmanager
    def timer(msg):
        start = time.time()
        yield
        end = time.time()
        print(f"%s: %.02fms" % (msg, (end-start)*1000))

    # Example usage
    sp = ScreenPixel()

    with timer("Capture"):
        # Take screenshot (takes about 70ms for me)
        sp.capture()

    with timer("Query"):
        # Get pixel value (takes about 0.01ms)
        print(sp.width, sp.height)
        print(sp.pixel(424, 682))


    # To verify screen-cap code is correct, save all pixels to PNG,
    # using http://the.taoofmac.com/space/projects/PNGCanvas

    # from pngcanvas import PNGCanvas
    # c = PNGCanvas(sp.width, sp.height)
    # for x in range(sp.width):
    #     for y in range(sp.height):
    #         c.point(x, y, color = sp.pixel(x, y))

    # with open("test.png", "wb") as f:
    #     f.write(c.dump())