import { isIPv6 } from "./isIpv6";

export function IP6to4(ip6: string) {
  function parseIp6(ip6str: string) {
    const str = ip6str.toString();

    // Initialize
    const ar = new Array();
    for (var i = 0; i < 8; i++) ar[i] = 0;

    // Check for trivial IPs
    if (str == "::") return ar;

    // Parse
    const sar = str.split(":");
    let slen = sar.length;
    if (slen > 8) slen = 8;
    let j = 0;
    i = 0;
    for (i = 0; i < slen; i++) {
      // This is a "::", switch to end-run mode
      if (i && sar[i] == "") {
        j = 9 - slen + i;
        continue;
      }
      ar[j] = parseInt(`0x0${sar[i]}`);
      j++;
    }

    return ar;
  }

  if (!isIPv6(ip6)) {
    return ip6;
  }

  var ip6parsed = parseIp6(ip6);
  const ip4 = `${ip6parsed[6] >> 8}.${ip6parsed[6] & 0xff}.${
    ip6parsed[7] >> 8
  }.${ip6parsed[7] & 0xff}`;
  return ip4;
}
