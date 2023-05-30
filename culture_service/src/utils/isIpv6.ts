export function isIPv6(address) {
    const ipv6Regex = /^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$/i;
    return ipv6Regex.test(address);
  }