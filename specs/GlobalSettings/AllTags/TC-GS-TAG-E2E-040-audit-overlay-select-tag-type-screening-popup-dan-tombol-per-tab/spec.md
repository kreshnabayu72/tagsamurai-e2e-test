---
id: TC-GS-TAG-E2E-040-audit-overlay-select-tag-type-screening-popup-dan-tombol-per-tab
title: "Audit TAG: Overlay Select TAG Type, Screening Popup Audit, Daftar Eligible, Combined, Empty State S-06, dan Tombol per Tab"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-117
  - TC-GS-TAG-118
  - TC-GS-TAG-119
  - TC-GS-TAG-120
  - TC-GS-TAG-121
  - TC-GS-TAG-122
  - TC-GS-TAG-137
coverage:
  web: automated
---

# Audit TAG: Overlay Select TAG Type, Screening Popup Audit, Daftar Eligible, Combined, Empty State S-06, dan Tombol per Tab

## Prerequisites

- Mode: FE+BE (backend nyata; seluruh langkah baca-saja, tanpa commit Audit).
- Akun aktor (tiga akun, ganti akun eksplisit; bagian sesudah ganti akun tetap bermakna):
  - Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` (TC-GS-TAG-137, 117, 118).
  - Total Control Client Audit Joko Santoso `totalControl_automated_qaAudit@qwertysystem.net`, `Spectra.env.GS_TC_AUDIT_PASSWORD` (TC-GS-TAG-119, 120, 121). Nama env belum terdaftar di `spectra.config.ts` dan `.env.example` (didaftarkan pemilik repositori).
  - Total Control Client Empty Budi Santoso `totalControl_automated_qaEmpty@qwertysystem.net`, `Spectra.env.GS_TC_EMPTY_PASSWORD` (TC-GS-TAG-122).
  - Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: Client A memuat Seed Registri A (tidak diubah spec ini). Client Empty tidak punya tag. Seed Client Audit (dipulihkan lewat fixture BE sebelum spec, tidak diubah spec ini):

  | Alias | Code | TAG Type | Status |
  |---|---|---|---|
  | AU1 (DD-31) | `E2801160600002054D8A5001` | RFID Object | Available (combined dengan AUN) |
  | AU2 (DD-32) | `E2801160600002054D8A5002` | RFID Object | Damaged/Missing |
  | AU3 (DD-33) | `E2801160600002054D8A5003` | RFID Object | Retired |
  | AU4 (DD-34) | `E2801160600002054D8A5004` | RFID Object | Available |
  | AU5 (DD-35) | `E2801160600002054D8A5005` | RFID Object | Reserved |
  | AU6 (DD-36) | `E2801160600002054D8A5006` | RFID Object | Paired |
  | AU7 (DD-37) | `E2801160600002054D8A5007` | RFID Object | To be Returned |
  | AUN (DD-38) | `04A224B2C15E95` | NFC | Available (combined dengan AU1) |

- Kemampuan teknis (disediakan tim FE/BE): seed/reset Seed Client Audit; mengubah ukuran viewport dan memulihkannya (agar scroll internal teramati dengan 4 baris, Q-11); selektor overlay Select TAG Type, ikon 🔗, dan popup Audit disediakan tim FE (belum ada ID/aria-label di sumber).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): pulihkan viewport, kembalikan sesi ke akun default suite.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Suite serial (`parallel: false`). Spec tidak mengubah state global. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-TAG-137: Tombol Audit TAG per tab (Client A)

1. Verifikasi tombol `Audit TAG` tampil pada toolbar Tab All
2. Klik Tab Not Paired
3. Verifikasi tombol `Audit TAG` tampil pada toolbar Tab Not Paired
4. Klik Tab Paired
5. Verifikasi toolbar Tab Paired tampil
6. Verifikasi tombol `Audit TAG` Hidden pada toolbar Tab Paired

### TC-GS-TAG-117: Overlay Select TAG Type Audit hanya menawarkan RFID dan NFC

7. Klik Tab All, lalu klik `Audit TAG`
8. Verifikasi overlay `Select TAG Type` single-select dengan pilihan `RFID` dan `NFC`
9. Verifikasi pilihan BLE dan GPS tidak ada

### TC-GS-TAG-118: Esc menutup overlay Audit tanpa membuka popup

10. Tekan `Esc`
11. Verifikasi overlay tertutup
12. Verifikasi tidak ada popup Audit TAG
13. Klik `Audit TAG` lagi
14. Verifikasi overlay `Select TAG Type` tampil tanpa pilihan terpilih (tidak ada tipe terkunci)
15. Tekan `Esc`

### TC-GS-TAG-119: Screening Popup Audit TAG (Client Audit)

16. Ganti akun: logout, lalu login sebagai Total Control Client Audit dengan `Spectra.env.GS_TC_AUDIT_PASSWORD`
17. Buka Global Settings > TAG > Tab Not Paired, klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
18. Verifikasi judul popup `Audit TAG`
19. Verifikasi header popup memuat tombol tutup `[✕]`
20. Verifikasi header popup tidak memuat penghitung langsung (live counter)
21. Verifikasi kolom tabel berurutan: `Device Name`, `SKU`, `Code`, `Status`, `Audit Status`, `Actions`
22. Verifikasi seluruh header kolom tidak sortable
23. Verifikasi header `Actions` memuat trigger Column Visibility
24. Verifikasi empat baris eligible berurutan Code A-Z: `E2801160600002054D8A5001`, `E2801160600002054D8A5002`, `E2801160600002054D8A5003`, `E2801160600002054D8A5004`
25. Verifikasi keempat baris berlencana `Not Scanned`
26. Verifikasi Device Name terisi pada keempat baris
27. Verifikasi tidak ada pagination
28. Perkecil viewport hingga keempat baris tidak muat seluruhnya
29. Verifikasi tabel memakai scroll internal dengan header tetap
30. Pulihkan viewport ke ukuran awal
31. Verifikasi sel `Actions` di setiap baris kosong (tanpa row action dan tanpa undo)
32. Verifikasi tombol [Submit] enabled

### TC-GS-TAG-120: Daftar Audit hanya memuat tag Not Paired berstatus Available, Damaged/Missing, atau Retired

33. Verifikasi daftar hanya memuat AU1, AU2, AU3, AU4
34. Verifikasi `E2801160600002054D8A5005` (AU5 Reserved), `E2801160600002054D8A5006` (AU6 Paired), dan `E2801160600002054D8A5007` (AU7 To be Returned) tidak ada di daftar

### TC-GS-TAG-121: Tag combined tampil dengan ikon 🔗 murni penanda visual

35. Verifikasi baris AU1 `E2801160600002054D8A5001` menampilkan ikon 🔗 di sebelah Code
36. Klik ikon 🔗 pada baris AU1
37. Verifikasi klik ikon tidak membuka popup apa pun
38. Klik `[✕]` pada popup Audit (tanpa baris Verified, popup tertutup langsung)

### TC-GS-TAG-122: Popup Audit tanpa tag eligible menampilkan empty state S-06 (Client Empty)

39. Ganti akun: logout, lalu login sebagai Total Control Client Empty dengan `Spectra.env.GS_TC_EMPTY_PASSWORD`
40. Buka Global Settings > TAG > Tab All, klik `Audit TAG`, lalu pilih `NFC` pada overlay `Select TAG Type`
41. Verifikasi popup terbuka dengan empty state berjudul `No TAGs to audit`
42. Verifikasi deskripsi empty state "There are no TAGs of this type waiting to be audited."
43. Verifikasi tombol [Submit] disabled

## Notes

- Mode: FE+BE. Spec melewati sekitar 35 langkah (43 langkah). Alasan: seluruh blok satu kelas (screening Audit TAG, baca-saja, tanpa commit) dan berdiri sendiri; ganti akun eksplisit pada langkah 16 dan 39 sah karena bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal (bagian 3, pemisah (b)). Tiga akun dipakai karena tiap TC menyebut client-nya sendiri.
- Urutan: TC-GS-TAG-137 (screening tombol) di awal, lalu TC-GS-TAG-117 dan 118, lalu blok Client Audit (119, 120, 121 dalam satu popup), terakhir Client Empty.
- Langkah penghubung (tanpa `Verifikasi`, S-03): 7, 13, 15, 16, 17, 28, 30, 38, 39, 40 (pindah tab, membuka overlay dan popup, ganti akun, perubahan viewport, menutup popup). Langkah 5 adalah anchor permukaan untuk asersi Hidden langkah 6.
- Pembagian TC lintas spec: TC-GS-TAG-123 sampai 126 (pemindaian) berada di spec 041; TC-GS-TAG-168 (Setup Column surface sekunder) berada di spec Setup Column (slice 6); TC-GS-TAG-175 (Free plan: Audit) berada di spec sendiri (slice 1).
- Temuan untuk QA:
  - TC-GS-TAG-118 Expected "tidak ada tipe terkunci" tidak punya cara observasi di TC; spec membuka kembali overlay dan mengasersi tidak ada pilihan terpilih (langkah 13 sampai 14), langkah tambahan yang dicatat di sini.
  - TC-GS-TAG-119 Expected d ("scroll internal dengan header tetap") tidak teramati dengan hanya 4 baris pada viewport standar; spec memperkecil viewport (kemampuan disediakan tim FE, Q-11).
  - TC-GS-TAG-119 Expected a menyebut "tidak ada penghitung langsung (live counter)" tanpa menyebut lokasinya; spec mengasersi pada header popup.
  - TC-GS-TAG-122 memakai Client Empty dengan precondition "User berada di Tab All"; email dan env mengikuti Pre-setup dan `.env.example`.
  - Post Condition semua TC bernilai `-`.
