---
id: TC-AC-ACAL-E2E-018-tab-session-setup-column-visibilitas-kolom-dan-persistensi
title: "Tab Session — Check/Uncheck visibilitas 10 kolom, Live Preview, dan persistensi reload F5"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-85
  - TC-AC-ACAL-86
  - TC-AC-ACAL-87
  - TC-AC-ACAL-88
  - TC-AC-ACAL-89
  - TC-AC-ACAL-90
  - TC-AC-ACAL-91
  - TC-AC-ACAL-92
  - TC-AC-ACAL-93
  - TC-AC-ACAL-94
coverage:
  web: automated
---

# Tab Session — Check/Uncheck visibilitas 10 kolom, Live Preview, dan persistensi reload F5

## Prerequisites

- Login sebagai Role: Principal Total Control
- Pengguna berada di `Admin Console > Activity Log` (Tab Session)

## Test Steps

### Uji Uncheck Kolom & Live Preview

1. Klik header kolom `⋯` > klik `"Setup Column"`
2. Uncheck kolom `Date`
3. Verifikasi kolom Date langsung hilang dari panel Live Preview secara real-time
4. Uncheck kolom `User`, `Employee ID`, `Position`, dan `Division`
5. Verifikasi seluruh kolom tersebut hilang dari Live Preview
6. Uncheck kolom `Activity`, `Status`, `Note`, `IP Address`, dan `Device / Browser`
7. Check kembali beberapa kolom (misal: `Date`, `User`, `Status`, `IP Address`)
8. Klik tombol `[Save]`
9. Verifikasi modal tertutup dan tabel Tab Session hanya menampilkan kolom yang tercentang

### Uji Persistensi Reload Browser (F5)

10. Lakukan refresh halaman browser (F5)
11. Verifikasi tabel Tab Session tetap mempertahankan konfigurasi visibilitas kolom yang telah disimpan (tidak kembali ke default)

## Notes

- Konfigurasi Setup Column disimpan di storage lokal browser pengguna dan harus persisten terhadap refresh halaman.
