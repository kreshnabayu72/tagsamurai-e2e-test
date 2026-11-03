---
id: TC-FA-FAAM-E2E-167-total-assets-hover-strip-kolom-label-dan-paginasi
title: "Tab Total Assets: Hover Badge, Strip Brand-Model Kosong, Tampilan Kolom Label, dan Paginasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-522
  - TC-FA-FAAM-667
  - TC-FA-FAAM-685
  - TC-FA-FAAM-717
coverage:
  web: automated
---

# Tab Total Assets: Hover Badge, Strip Brand-Model Kosong, Tampilan Kolom Label, dan Paginasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Dell Latitude` (Total Asset 42, Pre-setup #26; setiap aset berlabel `Finance` dan `High Priority`, aset `Dell Latitude - 42` diberi tambahan label `Fragile`), `Unlabeled Asset Item` (Total Asset 1, aset `AST-1301` tanpa label, Pre-setup #26f), `Long Badge Item` (Total Asset 1, Brand `Long Brand Name Twenty-Six`, model `Long Model Name Twenty Six`, aset di Group `Finance` subgroup dari `Head Office`, Pre-setup #26d), `Blank Brand Item` (Total Asset 1, aset `AST-1201` tanpa Brand dan Model/Type, dibuat lewat seed API langsung karena Registrasi Aset mewajibkan Brand dan Model/Type, Pre-setup #26e).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-522: Paginasi Tab Total Assets

1. Klik nama `Dell Latitude`, klik tab `Total Assets (42)`
2. Verifikasi footer menampilkan default 10 baris per halaman
3. Buka pilihan page size pada footer
4. Verifikasi pilihan page size 10, 25, 50, dan 100
5. Ubah page size ke 25
6. Pindah ke halaman 2
7. Verifikasi label tab tetap `Total Assets (42)`

### TC-FA-FAAM-717: Tampilan kolom Label (chip berwarna, +N more, popover, strip bila kosong)

8. Klik header Actions (⋯), pilih `Setup Column...`, centang Label, klik `[Save]` (precondition TC: kolom curated Label sudah ditampilkan; dipakai sebagai precondition, tidak diasersi)
9. Ketik Search `Dell Latitude - 42`, tekan Enter
10. Verifikasi kolom Label `Dell Latitude - 42` menampilkan chip berwarna label `Finance` dan `Fragile` lalu chip `+1 more` (urut A–Z)
11. Klik `(←)` pada kotak Search
12. Verifikasi sedikitnya satu baris aset lain tampil
13. Verifikasi aset lain menampilkan chip `Finance` dan `High Priority` tanpa `+N more`
14. Ketik Search `Dell Latitude - 42`, tekan Enter
15. Klik chip `+1 more` pada baris `Dell Latitude - 42`
16. Verifikasi popover "Labels" berisi badge penuh `Finance`, `Fragile`, `High Priority` berwarna label tanpa truncation (urut A–Z)
17. Klik di luar popover
18. Verifikasi popover tertutup
19. Tutup popup Detail
20. Ketik Search `Unlabeled Asset Item`, tekan Enter
21. Klik nama `Unlabeled Asset Item`, klik tab `Total Assets (1)`
22. Verifikasi kolom Label aset `AST-1301` menampilkan `—` (bukan blank)
23. Tutup popup Detail, klik `(←)` pada kotak Search

### TC-FA-FAAM-667: Hover Brand, Model/Type, dan Group menampilkan nama penuh badge dan hierarki Group

24. Klik nama `Long Badge Item`, klik tab `Total Assets (1)`
25. Verifikasi badge Brand tampil `Long Brand N..e Twenty-Six`
26. Hover badge Brand pada baris aset
27. Verifikasi hover Brand menampilkan nama penuh `Long Brand Name Twenty-Six`
28. Verifikasi badge Model/Type tampil `Long Model N..e Twenty Six`
29. Hover badge Model/Type pada baris aset
30. Verifikasi hover Model/Type menampilkan nama penuh `Long Model Name Twenty Six`
31. Hover badge Group pada baris aset
32. Verifikasi hover Group menampilkan hierarki penuh `Head Office > Finance`
33. Tutup popup Detail

### TC-FA-FAAM-685: Brand dan Model/Type aset yang kosong tampil strip

34. Klik nama `Blank Brand Item`, klik tab `Total Assets (1)`
35. Verifikasi sel Brand baris `AST-1201` menampilkan `—` karena aset ini tidak memiliki nilai Brand
36. Verifikasi sel Model/Type baris `AST-1201` menampilkan `—` karena aset ini tidak memiliki nilai Model/Type

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 522, 717, 667, 685. TC-FA-FAAM-717 menyimpan konfigurasi kolom Label sehingga ditaruh sesudah 522; TC-FA-FAAM-667 dan 685 memakai fixture masing-masing dan dikerjakan sesudahnya.
- Langkah penghubung: centang Label dan Search `Dell Latitude - 42` untuk menemukan baris target beserta `(←)` pada blok TC-FA-FAAM-717; menutup popup Detail sebelum berpindah fixture; Search `Unlabeled Asset Item` pada langkah 20 (dibersihkan dengan `(←)` pada langkah 23) agar baris berada di halaman 1 daftar A-Z yang diawali 30 `Seed Item` (R-16).
- Rujukan `(←)` pada Search mengosongkan kotak Search dan mereset tabel (bagian 8b butir 9).
- Di atas smell 35 langkah. Spec berjumlah 36 langkah (melewati sekitar 35). Empat blok memakai fixture masing-masing dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-FAAM-717 mengharapkan kolom Label sudah ditampilkan (precondition) tanpa langkah memunculkannya di LK; spec menambah langkah penghubung centang Label.
  - TC-FA-FAAM-522 butir c ("Label `[N]` tetap 42") hanya mengasersi label tab; TC tidak menyebut jumlah baris halaman 2.
