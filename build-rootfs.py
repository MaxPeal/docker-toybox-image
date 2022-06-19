import urllib.request
import os
import platform
import subprocess

os.makedirs('rootfs/bin')
os.makedirs('rootfs/sbin')
os.makedirs('rootfs/usr/bin')
os.makedirs('rootfs/usr/sbin')

print(platform.architecture())
print(platform.machine())
print(platform.node())
print(platform.platform())
print(platform.processor())
print(platform.system())
#print(platform.system_alias())
print(platform.uname())
print(platform.freedesktop_os_release())

toybox_arch_mapping = {
    'aarch64': 'aarch64',
    'armv7l': 'armv7l',
    'armv6l': 'armv6l',
    'armv5l': 'armv5l',
    'armv4l': 'armv4l',
#    'armv7l': 'armv4l',
#    'mips64le': 'mips64le',
    'mips64': 'mips64le',
    'ppc64le': 'powerpc64le',
    'riscv64': 'riscv64',
    's390x': 's390x',
    'i386': 'i486',
    'x86_64': 'x86_64'
}

# print('http://landley.net/toybox/bin/toybox-{toybox_arch_mapping[platform.machine()]}')

with urllib.request.urlopen(f'http://landley.net/toybox/bin/toybox-{toybox_arch_mapping[platform.machine()]}') as f:
    # print(f)
    toybox = f.read()
    with open('rootfs/bin/toybox', 'wb') as file:
        file.write(toybox)
        os.chmod('rootfs/bin/toybox', 0o777)
    toybox_commands = subprocess.run(['rootfs/bin/toybox', '--long'], capture_output=True, text=True).stdout.split()
    print(toybox_commands)
    for c in toybox_commands:
        print(c)
        os.symlink('/bin/toybox', f'rootfs/{c}')
