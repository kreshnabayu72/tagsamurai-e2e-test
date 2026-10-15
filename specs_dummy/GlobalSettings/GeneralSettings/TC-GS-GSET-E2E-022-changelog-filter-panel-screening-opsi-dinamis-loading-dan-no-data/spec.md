---
id: TC-GS-GSET-E2E-022-changelog-filter-panel-screening-opsi-dinamis-loading-dan-no-data
title: "Filter Panel Changelog: screening, opsi Field/Modified By dari baris, search internal, opsi dinamis, indikator loading, dan no-options"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-GSET-71
  - TC-GS-GSET-72
  - TC-GS-GSET-75
  - TC-GS-GSET-80
  - TC-GS-GSET-150
  - TC-GS-GSET-174
  - TC-GS-GSET-177
  - TC-GS-GSET-178
coverage:
  web: automated
---

# Filter Panel Changelog: screening, opsi Field/Modified By dari baris, search internal, opsi dinamis, indikator loading, dan no-options

## Prerequisites

- Login sebagai Role: Total Control
- Changelog General Settings berisi baris riwayat (dinamis); Budi Santoso dan Andi Wijaya masing-masing punya ≥1 baris
- Entitas `Client Satu Riwayat` hanya punya 1 baris Changelog: Field `Session Idle Timeout` oleh Budi Santoso
- Entitas `Client Baru` tanpa Save General Settings (Changelog kosong)
- Spectra.intercept() dikonfigurasi untuk menahan (delay 5 detik) respons pengambilan opsi dropdown filter

## Test Steps

### Screening Filter Panel

1. Buka Modal Changelog, klik Filter, dan amati panel
2. Verifikasi 3 field: Date (date range picker, placeholder "Select date"), Field (multi-select searchable, placeholder "All fields"), Modified By (multi-select searchable, placeholder "All users")
3. Verifikasi Actions: `[Clear Field]` (kiri) dan `[Apply]` (kanan), tanpa filter Action

### Opsi Field dan Modified By dari Baris Entitas

4. Login sebagai staff `Client Satu Riwayat`, buka Modal Changelog > Filter, lalu buka dropdown Field
5. Verifikasi opsi hanya `Session Idle Timeout`; `Currency Code`, `Time Zone`, `Date Format`, `Time Format` tidak tampil; tidak ada opsi `Currency Symbol`
6. Buka dropdown Modified By
7. Verifikasi opsi hanya `Budi S`; user `Andi W` tidak tampil di opsi

### Search Internal Dropdown Field

8. Kembali sebagai Total Control dengan data riwayat, buka Filter dan dropdown Field
9. Ketik "Time" di kotak pencarian dropdown
10. Verifikasi opsi menyempit ke `Time Zone` dan `Time Format`
11. Ketik "zzzz"
12. Verifikasi tidak ada opsi cocok

### Search Internal dan OR dalam Satu Field Modified By

13. Buka dropdown Modified By, amati placeholder (verifikasi "All users")
14. Ketik "Andi"; verifikasi opsi menyempit ke `Andi W`
15. Ketik "zzzz"; verifikasi tidak ada opsi cocok
16. Hapus kata kunci, centang `Budi S` dan `Andi W`
17. Verifikasi chip `Budi S` dan `Andi W` tampil di dalam field
18. Klik `[Apply]`; verifikasi tabel menampilkan baris Modified By `Budi S` ATAU `Andi W`

### Opsi Dinamis Tanpa Reload

19. Admin A (staff `Client Satu Riwayat`) membuka Modal Changelog > Filter dan mengamati opsi Field dan Modified By
20. Admin B memilih Time Format `hh:mm a` lalu klik `[Save]`
21. Admin A menutup lalu membuka kembali Filter pada Modal Changelog yang sama (tanpa reload)
22. Verifikasi Field bertambah `Time Format` dan Modified By bertambah `Andi W`

### Indikator Loading Opsi

23. Aktifkan delay 5 detik pada respons pengambilan opsi dropdown filter
24. Buka Modal Changelog > Filter lalu buka dropdown Field
25. Verifikasi skeleton atau spinner mini tampil selama opsi diambil (bukan dropdown kosong)
26. Tunggu respons; verifikasi opsi Field tampil
27. Aktifkan delay lagi, buka dropdown Modified By, dan verifikasi skeleton/spinner mini tampil

### No Options Available

28. Login sebagai staff `Client Baru`, buka Modal Changelog > Filter, lalu buka dropdown Field
29. Verifikasi teks "No options available" (bukan error, bukan daftar kelima nilai Field)
30. Buka dropdown Modified By dan verifikasi teks "No options available"

## Notes

- Menggabungkan TC-GS-GSET-71, 72, 75, 80, 150, 174, 177, dan 178 (Filter Panel beserta sumber opsi dinamis). Langkah 20–22 melibatkan Admin B pada entitas sama.
