extension = input("File name:").strip().lower()

if "gif" in extension:
    print("image/gif")
elif "jpg" in extension:
    print("image/jpeg")
elif "jpeg" in extension:
    print("image/jpeg")
elif "pdf" in extension:
    print("application/pdf")
elif "png" in extension:
    print("image/png")
elif ".txt" in extension:
    print("text/plain")
elif ".zip" in extension:
    print("application/zip")
else:
    print("application/octet-stream ")


