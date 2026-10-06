---
id: TC-AC-ACAL-E2E-032-tab-user-action-setup-column-visibilitas-kolom-dan-persistensi
title: "Tab User Action — Check/Uncheck visibilitas 8 kolom, Live Preview, dan persistensi reload F5"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-176
  - TC-AC-ACAL-177
  - TC-AC-ACAL-178
  - TC-AC-ACAL-179
  - TC-AC-ACAL-180
  - TC-AC-ACAL-181
  - TC-AC-ACAL-182
  - TC-AC-ACAL-183
coverage:
  web: automated
---

# Tab User Action — Check/Uncheck visibilitas 8 kolom, Live Preview, dan persistensi reload F5

## Prerequisites

- Login sebagai Role: Principal Total Control
- Pengguna berada di `Admin Console > Activity Log` (Tab User Action)

## Test Steps

### Uji Uncheck Kolom & Live Preview

1. Klik header kolom `⋯` > klik `"Setup Column"`
2. Uncheck kolom `Date`
3. Verifikasi kolom Date langsung hilang dari panel Live Preview secara real-time
4. Uncheck kolom `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, dan `Modified By`
5. Verifikasi seluruh kolom tersebut hilang dari Live Preview
6. Check kembali kolom `Date`, `Action`, `Object`, dan `Modified By`
7. Klik tombol `[Save]`
8. Verifikasi modal tertutup dan tabel Tab User Action hanya menampilkan kolom yang dipilih

### Uji Persistensi Reload Browser (F5)

9. Lakukan refresh halaman browser (F5)
10. Verifikasi tabel Tab User Action tetap mempertahankan konfigurasi visibilitas kolom yang telah disimpan

## Notes

- Memverifikasi penyimpanan state visibilitas kolom Tab User Action di storage lokal.
