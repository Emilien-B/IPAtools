
while True:
    bundle_version = str(input("Enter the bundle version "))
    
    def test(bundle_verion):
        for a in bundle_version.split('.'):
            try:
                a = int(a)
            except:
                return "Invalid bundle version"
                break
            return "Valid bundle version"
    bundle_version = str(input("Enter the bundle version "))
    print(test(bundle_version))