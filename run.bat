@echo off
Raytracing.exe > image.ppm

IF EXIST image.ppm (
    echo File image.ppm created successfully.
    python converter.py image.ppm output.png

    IF EXIST output.png (
        start output.png
    ) ELSE (
        echo output.png not found after conversion
        pause
    )
) ELSE (
    echo image.ppm not found
    pause
)