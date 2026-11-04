---
id: TC-FA-LBL-E2E-039-labels-list-setup-column-pin-dan-reset-to-default
title: "Labels List: Setup Column (pin kolom dan Reset to Default)"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-01/setup-column/pin
  - FALB:obl/T-ALB-01/setup-column/reset
coverage:
  web: automated
---

# Labels List: Setup Column (pin kolom dan Reset to Default)

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-56` (12 label bersuffix `Lst-{runId}-039-01` sampai `Lst-{runId}-039-12`, dipakai agar tabel memuat baris data).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label dan aset; penghapusan preferensi kolom tersimpan di browser untuk tabel Labels List di hook `after`.
- State global: konfigurasi kolom Labels List tersimpan di browser (bukan di server). Blok reset (langkah 17 sampai 22) memulihkan susunan bawaan; hook `after` menghapus preferensi kolom sebagai cadangan dan menghapus label seed `DU-56` lewat sesi API.

## Test Steps

1. Ketik Search `DU-56` (nama dasar `Lst-{runId}-039`), tekan Enter

### FALB:obl/T-ALB-01/setup-column/pin: Pin kolom dan batas pin

2. Klik header kolom Actions (`⋯`) pada Labels List, pilih `Setup Column...`
3. Klik ikon Pin pada kolom Label
4. Klik ikon Pin pada kolom Color Hex
5. Klik ikon Pin pada kolom Total Asset
6. Verifikasi ikon Pin kolom Modified By dan Last Updated Disabled
7. Arahkan kursor ke ikon Pin kolom Modified By
8. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.` tampil
9. Klik `[Save]`
10. Persempit lebar viewport browser hingga tabel Labels List dapat digulir horizontal
11. Gulir tabel Labels List ke kanan
12. Verifikasi kolom Label, Color Hex, dan Total Asset tetap berada di sisi kiri tabel tanpa ikut bergeser saat tabel digulir
13. Pulihkan lebar viewport browser
14. Klik header kolom Actions (`⋯`) pada Labels List, pilih `Setup Column...`
15. Klik ikon Pin pada kolom Label untuk melepas pin
16. Verifikasi ikon Pin kolom Modified By dan Last Updated kembali Enabled

### FALB:obl/T-ALB-01/setup-column/reset: Reset to Default

17. Hapus centang kolom Last Updated
18. Geser kolom Total Asset ke posisi pertama pada daftar kolom Modal Setup Column
19. Klik `[Reset to Default]`
20. Verifikasi pratinjau tabel di balik modal menampilkan kelima kolom Label, Color Hex, Total Asset, Modified By, dan Last Updated tercentang berurutan bawaan dan tidak ada kolom yang di-pin
21. Klik `[Save]`
22. Verifikasi Labels List menampilkan header kolom berurutan `Label | Color Hex | Total Asset | Modified By | Last Updated`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit tabel ke label `DU-56`, R-16), langkah 2 dan 14 (membuka Modal Setup Column), langkah 10 dan 13 (mengatur lebar viewport), langkah 11 (menggulir tabel).
- Pemulihan Setup Column (8b.14, R-24): langkah 15 melepas pin kolom Label pada sesi modal yang sama dengan blok reset; langkah 19 sampai 22 mengembalikan seluruh visibilitas, urutan, dan pin ke susunan bawaan dengan `Verifikasi` hasil reset karena itu klausa aturan reset.
- Langkah 17 dan 18 menyiapkan perubahan (sembunyikan dan geser) yang dipulihkan klausa reset; pin kolom Color Hex dan Total Asset dari langkah 4 dan 5 juga dipulihkan reset (langkah 20).
- Hide-show dan reorder ada di spec 031.
