---
id: TC-FA-LBL-E2E-031-labels-list-setup-column-sembunyikan-dan-geser
title: "Labels List: Setup Column (sembunyikan, tampilkan, dan geser kolom)"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-01/setup-column/hide-show
  - FALB:obl/T-ALB-01/setup-column/reorder
coverage:
  web: automated
---

# Labels List: Setup Column (sembunyikan, tampilkan, dan geser kolom)

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-56` (12 label bersuffix `Lst-{runId}-031-01` sampai `Lst-{runId}-031-12`, dipakai agar pratinjau dan tabel memuat baris data).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label dan aset; penghapusan preferensi kolom tersimpan di browser untuk tabel Labels List di hook `after`.
- State global: konfigurasi kolom Labels List tersimpan di browser (bukan di server). Spec memulihkannya ke susunan bawaan lewat langkah 15 sampai 21 dan 28 sampai 30; hook `after` menghapus preferensi kolom sebagai cadangan dan menghapus label seed `DU-56` lewat sesi API.

## Test Steps

1. Ketik Search `DU-56` (nama dasar `Lst-{runId}-031`), tekan Enter

### FALB:obl/T-ALB-01/setup-column/hide-show: Sembunyikan dan tampilkan kolom Hideable

2. Klik header kolom Actions (`⋯`) pada Labels List, pilih `Setup Column...`
3. Verifikasi Modal `Setup Column` memuat kelima kolom Hideable Label, Color Hex, Total Asset, Modified By, dan Last Updated dalam keadaan tercentang
4. Hapus centang kolom Color Hex
5. Hapus centang kolom Total Asset
6. Hapus centang kolom Modified By
7. Hapus centang kolom Last Updated
8. Verifikasi header kolom Label tampil pada tabel di balik modal
9. Verifikasi header kolom Color Hex, Total Asset, Modified By, dan Last Updated tidak tampil pada tabel di balik modal
10. Verifikasi checkbox kolom Label Disabled karena menjadi satu-satunya kolom visible
11. Arahkan kursor ke checkbox kolom Label
12. Verifikasi tooltip `At least one column must remain visible.` tampil
13. Klik `[Save]`
14. Verifikasi Labels List hanya menampilkan header kolom Label
15. Klik header kolom Actions (`⋯`) pada Labels List, pilih `Setup Column...`
16. Centang kolom Color Hex
17. Centang kolom Total Asset
18. Centang kolom Modified By
19. Centang kolom Last Updated
20. Verifikasi tabel di balik modal menampilkan kembali header kolom Color Hex, Total Asset, Modified By, dan Last Updated
21. Klik `[Save]`
22. Verifikasi Labels List menampilkan header kolom berurutan `Label | Color Hex | Total Asset | Modified By | Last Updated`

### FALB:obl/T-ALB-01/setup-column/reorder: Geser urutan kolom

23. Klik header kolom Actions (`⋯`) pada Labels List, pilih `Setup Column...`
24. Geser kolom Last Updated ke posisi pertama pada daftar kolom Modal Setup Column
25. Verifikasi tabel di balik modal menampilkan header kolom berurutan `Last Updated | Label | Color Hex | Total Asset | Modified By`
26. Klik `[Save]`
27. Verifikasi Labels List menampilkan header kolom berurutan `Last Updated | Label | Color Hex | Total Asset | Modified By`
28. Klik header kolom Actions (`⋯`) pada Labels List, pilih `Setup Column...`
29. Geser kolom Last Updated kembali ke posisi terakhir pada daftar kolom Modal Setup Column
30. Klik `[Save]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit tabel ke label `DU-56`, R-16) dan langkah 2, 15, 23, serta 28 (membuka Modal Setup Column).
- Pemulihan Setup Column (8b.14, R-24): langkah 15 sampai 21 memulihkan visibilitas keempat kolom (dengan `Verifikasi` kolom tampil kembali, karena menampilkan kolom adalah klausa aturan hide-show); langkah 28 sampai 30 memulihkan urutan kolom tanpa `Verifikasi`.
- Spec ini satu kelas harness (Setup Column) dan memakai dataset yang sama; setiap blok dimulai dengan membuka Modal Setup Column dan mengembalikan konfigurasi ke susunan bawaan sebelum blok berikutnya, sehingga blok berdiri sendiri. Pin kolom dan `[Reset to Default]` ada di spec 039.
