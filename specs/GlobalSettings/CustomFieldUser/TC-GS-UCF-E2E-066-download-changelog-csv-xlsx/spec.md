---
id: TC-GS-UCF-E2E-066-download-changelog-csv-xlsx
title: "Download Changelog Custom Field CSV dan XLSX: Mengikuti Search dan Filter, Isi Sel, Seluruh Entri Lintas Halaman, dan Kolom Hidden"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-272
  - TC-GS-UCF-530
  - TC-GS-UCF-531
  - TC-GS-UCF-532
coverage:
  web: automated
---

# Download Changelog Custom Field CSV dan XLSX: Mengikuti Search dan Filter, Isi Sel, Seluruh Entri Lintas Halaman, dan Kolom Hidden

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client A Sari Dewi (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; `## Test Steps` tidak mengulang langkah buka.
- Data Pre-setup (baca-saja, tidak diubah spec ini): 6 Custom Field Pre-setup Client A dan Changelog Pre-setup 8 entri bertanggal 8 sampai 11 Sep 2026 (fixture backend): Edit `Cost Center — Value Setting` (Budi S, Old `Finance, Operations`, New `Finance, Operations, Marketing`), Create `Cost Center`, Activate `Employee Grade — Status` (Siti R), Deactivate `Joining Date — Status`, Delete `Legacy Field` (Siti R), Create `Job Description` (Siti R), Create `Bonus`, Create `Office Phone`. Nama lengkap pelaku: `Budi Santoso` (Budi S), `Siti Rahmawati` (Siti R).
- Data Population (precondition TC): 8 Custom Field Population dibuat lewat API oleh Sari Dewi di hook `before` bila belum ada (seeding idempotent; 8 entri Create, Modified By `Sari D`). Total entri Changelog Client A untuk TC-GS-UCF-531 tidak dipatok mutlak (Changelog kumulatif): jumlah N dicatat dari Pagination pada langkah 36.
- General Settings Client A: Date Format `DDD, MMM dd, yyyy`, Time Format `hh:mm a` (precondition e TC-GS-UCF-530; nilai default fixture, tidak diubah spec ini).
- Setup Column Modal Changelog: konfigurasi default; hook `beforeEach` membersihkan cache browser. TC-GS-UCF-532 menyembunyikan lalu menampilkan kembali kolom `Old Value` dan `New Value`; hook `after` menjalankan `[Reset to Default]` sebagai cadangan.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis (kelas f, binary buffer): pembacaan jumlah total entri dari label Pagination (belum terbukti label menampilkan total; lihat Temuan untuk QA; langkah 36 dan 41); menangkap berkas unduhan di browser; pembaca berkas CSV (teks mentah termasuk bungkus kutip ganda) dan XLSX (sheet, header, baris data); deteksi ada atau tidaknya toast saat Download.
- State global: tidak ada yang diubah selain flag Guided Tooltip dan konfigurasi Setup Column Changelog (dipulihkan seperti di atas). Spec ini hanya membaca.

## Test Steps

### TC-GS-UCF-272: Download mengikuti Search dan Filter aktif

1. Klik icon Changelog
2. Klik Filter, pilih Date 8 Sep 2026 sampai 11 Sep 2026, klik `[Apply]`, lalu klik icon Filter untuk menutup panel
3. Ketik Search `Create`, tekan Enter
4. Klik Download > `Download as CSV`
5. Verifikasi tidak ada toast sukses
6. Verifikasi berkas `Changelog-Custom-Field.csv` terunduh
7. Buka berkas `Changelog-Custom-Field.csv` hasil unduhan
8. Verifikasi berkas CSV berisi 4 entri Create Pre-setup: `Cost Center`, `Job Description`, `Bonus`, dan `Office Phone`
9. Klik Download > `Download as XLSX`
10. Verifikasi tidak ada toast sukses
11. Verifikasi berkas `Changelog-Custom-Field.xlsx` terunduh
12. Buka berkas `Changelog-Custom-Field.xlsx` hasil unduhan
13. Verifikasi berkas XLSX berisi entri yang sama dengan CSV

### TC-GS-UCF-530: Isi sel file export: sel kosong, Modified By nama lengkap, format tanggal, dan nilai berkoma

14. Klik `(←)` pada kotak Search
15. Klik Download > `Download as CSV`
16. Buka berkas CSV sebagai teks mentah
17. Verifikasi baris header `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
18. Verifikasi 8 baris data (Filter Date 8 sampai 11 Sep 2026 masih aktif)
19. Verifikasi entri Create `Cost Center`: Old Value `-`
20. Verifikasi entri Create `Cost Center`: New Value `Cost Center`
21. Verifikasi entri Delete `Legacy Field`: Old Value `Legacy Field`
22. Verifikasi entri Delete `Legacy Field`: New Value `-`
23. Verifikasi Modified By entri Edit `Cost Center — Value Setting` memuat nama lengkap `Budi Santoso`
24. Verifikasi Modified By entri Activate `Employee Grade — Status` memuat nama lengkap `Siti Rahmawati`
25. Verifikasi kolom Date entri Edit `Cost Center — Value Setting` berpola `DDD, MMM dd, yyyy hh:mm a`
26. Verifikasi Old Value `Finance, Operations` pada entri Edit dibungkus tanda kutip ganda sehingga tidak terpecah ke kolom lain
27. Verifikasi New Value `Finance, Operations, Marketing` pada entri Edit dibungkus tanda kutip ganda sehingga tidak terpecah ke kolom lain

### TC-GS-UCF-532: Kolom hidden tidak ikut terunduh dan kembali setelah unhide

28. Klik Filter, klik `[Clear Field]`, klik `[Apply]`, lalu klik icon Filter untuk menutup panel
29. Klik header Column Visibility (⋯), uncheck `Old Value` dan `New Value`
30. Klik Download > `Download as CSV`, buka berkas
31. Verifikasi berkas memuat kolom `Date`, `Action`, `Field`, dan `Modified By`
32. Verifikasi berkas tidak memuat kolom `Old Value` dan `New Value`
33. Klik header Column Visibility (⋯), centang kembali `Old Value` dan `New Value`
34. Klik Download > `Download as CSV`, buka berkas
35. Verifikasi berkas memuat kolom `Date`, `Action`, `Field`, `Old Value`, `New Value`, dan `Modified By`

### TC-GS-UCF-531: Download tanpa Search dan Filter memuat seluruh entri lintas halaman

36. Catat jumlah total entri N dari Pagination (N > 10)
37. Klik Download > `Download as XLSX`
38. Verifikasi tidak ada toast sukses
39. Buka berkas `Changelog-Custom-Field.xlsx`
40. Verifikasi berkas memuat satu sheet `Sheet1`
41. Verifikasi berkas memuat N baris data (sama dengan total entri yang dicatat pada langkah 36), bukan hanya 10 entri halaman 1
42. Klik `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Spec melewati sekitar 35 langkah (smell, bagian 3 prinsip 13 konvensi): 4 TC satu topik (Download Changelog CSV/XLSX) dengan satu akun dan satu pembukaan modal; setiap Expected bermajemuk dipecah satu `Verifikasi` per klausa (S-01) dan blok per TC tetap bermakna bila blok sebelumnya gagal.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 272, 530, 532, 531. Urutan menyimpang dari urutan TC sumber: kasus yang memakai Filter Date aktif (272, 530) berurutan pada satu pembukaan modal, lalu filter dihapus untuk kasus tanpa Filter (532, 531); TC-GS-UCF-530 memakai Filter Date yang sudah aktif dari TC-GS-UCF-272 (menggantikan langkah 2 TC-GS-UCF-530; Search `Create` dilepas di langkah 14). Modal dibuka sekali (langkah 1) dan ditutup sekali (langkah 42).
- Absence toast (langkah 5, 10, 38) diletakkan segera sesudah pemicu Download dan sebelum asersi artefak; pemicu Download menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh (bagian 8b butir 11). Pada TC-GS-UCF-531 pemicunya langkah 37 dan buktinya langkah 39 sampai 41.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka modal), langkah 2, 14, 28 (memasang atau melepas Filter dan Search; langkah 2 dan 28 sekaligus menutup Filter Panel), langkah 7 dan 12 (membuka berkas CSV dan XLSX hasil unduhan sebelum `Verifikasi` isi berkas, S-14), langkah 16, 30, 34, 39 (membuka berkas), langkah 36 (mencatat N dari Pagination sebagai pembanding langkah 41), langkah 29 dan 33 (mengubah visibility kolom; kolom dikembalikan di langkah 33), langkah 42 (menutup modal lewat `[✕]`).
- Spec berjumlah 42 langkah, sedikit di atas ambang sekitar 35. Seluruhnya satu kelas f (isi berkas export Changelog) pada satu dataset baca-saja dan tiap blok TC berdiri sendiri; kegagalan satu blok tidak menghilangkan makna blok lain.
- Model Filter Panel (keputusan K-10 A, 2026-10-29): panel tetap terbuka sesudah `[Apply]`; `[Apply]` yang diikuti aksi di luar panel (Search, Column Visibility) ditutup lewat klik icon Filter (langkah 2 dan 28). Pola ini sama dengan spec 052, 053, dan 063.
- Kegagalan unduhan (500, timeout) ada di spec 060 (TC-GS-UCF-273 dan 553).
- Temuan untuk QA:
  - TC-GS-UCF-272 langkah 2 menulis "Klik Filter" dan TC-GS-UCF-532 memakai Filter yang sudah diterapkan; "Klik Filter" dapat berarti membuka ulang panel. Spec mengikuti K-10 A dengan menutup panel sesudah `[Apply]` lebih dulu: perlu konfirmasi QA/PRD.
  - TC-GS-UCF-530 Expected b dan c memakai token sel kosong `-` dan Expected d memakai nama lengkap (NC-11 menetapkan keduanya; LLD export masih memakai `—`). Per keputusan user, asersi mengikuti TC dan kemungkinan gagal sampai LLD diselaraskan: TC-GS-UCF-530 (NC-11). Berkas CSV dengan BOM (NC-12) tidak diasersi oleh TC-GS-UCF-530.
  - TC-GS-UCF-272 dan 531: nama berkas `Changelog-Custom-Field.csv` dan `.xlsx` dan toast tidak muncul (Expected c) mengikuti TC; PRD tidak diperiksa ulang oleh penulis spec.
  - TC-GS-UCF-531 (setelah perbaikan 2026-10-29, K-11 A) membandingkan jumlah baris berkas dengan N yang dicatat dari Pagination; label Pagination yang menampilkan total belum terbukti dan perlu konfirmasi QA.
  - TC-GS-UCF-530 Expected e (`DDD, MMM dd, yyyy hh:mm a`) bergantung pada precondition e (General Settings Client A); spec lain di suite yang mengubah format tanggal (spec 071) harus memulihkannya.
  - TC-GS-UCF-532 tidak menyatakan baris data yang diperiksa pada berkas; spec hanya mengasersi header kolom.
