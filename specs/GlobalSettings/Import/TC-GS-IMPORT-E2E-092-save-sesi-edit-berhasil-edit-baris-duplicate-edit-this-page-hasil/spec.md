---
id: TC-GS-IMPORT-E2E-092-save-sesi-edit-berhasil-edit-baris-duplicate-edit-this-page-hasil
title: "Save sesi edit berhasil: Edit Baris, Duplicate, Edit this page, hasil duplicate setelah Save, dan Code Division jadi error"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-209
  - TC-GS-IMPORT-210
  - TC-GS-IMPORT-211
  - TC-GS-IMPORT-215
  - TC-GS-IMPORT-216
  - TC-GS-IMPORT-217
  - TC-GS-IMPORT-652
coverage:
  web: automated
---

# Save sesi edit berhasil: Edit Baris, Duplicate, Edit this page, hasil duplicate setelah Save, dan Code Division jadi error

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Dinamis (nama literal karena asersi bergantung pada isi dan jumlah baris; pengecualian S-12): D-01 (Draft Brand 12 baris `pending`: #1 `Acme Corp`, #2 `Lenovo`, #3 `Zebra Technologies`, ..., #12 `Asus`) dan D-04 (Draft Division 6 baris `pending` dari `division-6.csv`: #1 `Finance & Accounting` Code `FIN`, #2 `Operations` Code kosong, lainnya sesuai berkas), dipulihkan oleh skrip pemulihan (Kontrak Fixture R2) sebelum tiap TC. Division `Engineering` Code `ENG` ada di sistem Client A (Pre-setup, tidak diubah). Nilai ubahan: `Acme Corporation`, `Lenovo Group`, `Lenovo`, `Acme Corp`, Code `FIN`, Code `ENG`.
- Kemampuan teknis: pengamatan toast, hover badge Status, skrip pemulihan draft Brand (D-01) dan Division (D-04) (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain draft Client A dan flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan draft Brand dan Division Client A ke D-01 dan D-04.

## Test Steps

### TC-GS-IMPORT-209: Save sesi Edit Baris yang valid

1. Klik `⋯` pada baris #1, pilih `Edit`
2. Ubah Brand Name baris #1 menjadi `Acme Corporation`
3. Klik `[Save]`
4. Verifikasi muncul toast sukses: "Success, row has been updated."
5. Verifikasi baris #1 menampilkan `Acme Corporation`
6. Verifikasi baris #1 berstatus `pending`
7. Verifikasi footer `[Import (12)]` tampil kembali (sesi tertutup)

### TC-GS-IMPORT-211: Save sesi Edit this page

8. Tunggu toast lama hilang otomatis; pulihkan draft Brand Client A ke D-01 lewat skrip pemulihan, lalu muat ulang halaman
9. Aktifkan Switch `Edit this page`
10. Ubah Brand Name baris #1 menjadi `Acme Corporation`
11. Ubah Brand Name baris #2 menjadi `Lenovo Group`
12. Klik `[Save]`
13. Verifikasi muncul toast sukses: "Success, row has been updated."
14. Verifikasi baris #1 `Acme Corporation` dan baris #2 `Lenovo Group` tersimpan berstatus `pending`
15. Verifikasi footer `[Import (12)]` tampil kembali (sesi berakhir)

### TC-GS-IMPORT-652: Baris atas disunting menjadi sama dengan baris bawah

16. Tunggu toast lama hilang otomatis; pulihkan draft Brand Client A ke D-01 lewat skrip pemulihan, lalu muat ulang halaman
17. Klik `⋯` pada baris #1, pilih `Edit`
18. Ubah Brand Name baris #1 menjadi `Lenovo`
19. Klik `[Save]`
20. Verifikasi muncul toast sukses: "Success, row has been updated."
21. Verifikasi baris #1 `Lenovo` berstatus `duplicate`
22. Verifikasi baris #2 `Lenovo` berstatus `pending`
23. Arahkan kursor ke badge Status baris #1
24. Verifikasi tooltip pada badge Status baris #1: "This row duplicates another row in this draft. It will be skipped automatically."
25. Verifikasi Staging Metric Cards: Duplicates 1, Ready to Import 11

### TC-GS-IMPORT-215: Baris bawah disunting menjadi sama dengan baris atas

26. Tunggu toast lama hilang otomatis; pulihkan draft Brand Client A ke D-01 lewat skrip pemulihan, lalu muat ulang halaman
27. Klik `⋯` pada baris #2, pilih `Edit`
28. Ubah Brand Name baris #2 menjadi `Acme Corp`
29. Klik `[Save]`
30. Verifikasi muncul toast sukses: "Success, row has been updated."
31. Verifikasi baris #1 `Acme Corp` berstatus `duplicate`
32. Verifikasi baris #2 `Acme Corp` berstatus `pending`
33. Arahkan kursor ke badge Status baris #1
34. Verifikasi tooltip pada badge Status baris #1: "This row duplicates another row in this draft. It will be skipped automatically."
35. Verifikasi Staging Metric Cards: Duplicates 1, Ready to Import 11

### TC-GS-IMPORT-216 dan TC-GS-IMPORT-217: Code Division jadi error setelah Save

36. Tunggu toast lama hilang otomatis; pilih Sub-Tab Division; pulihkan draft Division Client A ke D-04 lewat skrip pemulihan, lalu muat ulang halaman
37. Klik `⋯` pada baris #2 `Operations`, pilih `Edit`
38. Isi Code baris #2 dengan `FIN` (sama dengan Code baris #1 `Finance & Accounting`)
39. Klik `[Save]`
40. Verifikasi `[Save]` tidak diblokir dan muncul toast sukses: "Success, row has been updated."
41. Verifikasi baris #2 `Operations` berstatus `pending`
42. Verifikasi baris #1 `Finance & Accounting` berstatus `error`
43. Verifikasi pesan "Code already exists" pada baris #1
44. Tunggu toast lama hilang otomatis; pulihkan draft Division Client A ke D-04 lewat skrip pemulihan, lalu muat ulang halaman
45. Klik `⋯` pada baris #2 `Operations`, pilih `Edit`
46. Isi Code baris #2 dengan `ENG` (sama dengan Code Division `Engineering` di sistem)
47. Klik `[Save]`
48. Verifikasi `[Save]` tidak diblokir dan muncul toast sukses: "Success, row has been updated."
49. Verifikasi baris #2 `Operations` berstatus `error`
50. Verifikasi pesan "Code already exists" pada baris #2

### TC-GS-IMPORT-210: Save sesi Duplicate (menambah baris, dijalankan paling akhir)

51. Tunggu toast lama hilang otomatis; pilih Sub-Tab Brand; pulihkan draft Brand Client A ke D-01 lewat skrip pemulihan, lalu muat ulang halaman
52. Klik `⋯` pada baris #2, pilih `Duplicate`
53. Ubah Brand Name salinan menjadi `Lenovo Group`
54. Klik `[Save]`
55. Verifikasi muncul toast sukses: "Success, row has been added."
56. Verifikasi footer `[Import (13)]` (draft menjadi 13 baris)
57. Verifikasi salinan `Lenovo Group` tersimpan berstatus `pending` tepat di bawah baris sumber `Lenovo` (baris sumber tetap #2, salinan #3)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-211 sebelum TC-652 dan TC-215 (nilai baris #1 dan #2 berubah) dan TC-210 paling akhir karena menambah baris; TC-216 dan TC-217 dikelompokkan pada Sub-Tab Division (prinsip 3 bagian 3). Tiap TC memulihkan draft ke D-01 atau D-04 lewat skrip (langkah penghubung tanpa `Verifikasi`).
- Spec berisi 57 langkah. Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional) dan satu topik (Save sesi edit berhasil), tiap blok memulihkan draft dan membuka sesi sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-GS-IMPORT-212 sampai 214 dan 671 sampai 675 (Save diblokir) ada di spec 094 dan 095; TC-GS-IMPORT-220 sampai 223 dan 653 sampai 655 (Save tanpa perubahan) di spec 093.
- Temuan untuk QA:
  - TC-GS-IMPORT-216 dan 217 tidak menyebut isi lengkap D-04 selain baris #1 dan #2 (`division-6.csv` disediakan tim QA); spec hanya memakai baris #1 dan #2.
  - TC-GS-IMPORT-209 Post Condition ("Baris #1 bernilai `Acme Corporation` berstatus `pending`") sudah diasersi pada Expected b; TC-GS-IMPORT-210 Post Condition ("Draft Brand 13 baris") sudah diasersi pada Expected b. Post Condition lain tidak ada.
  - TC-GS-IMPORT-216 dan 217 Expected menyebut pesan "Code already exists" tanpa lokasi tampil (sel atau Callout); spec mengasersi pesan pada baris tersebut tanpa menyebut elemen.
  - TC-GS-IMPORT-215 dan 652 Expected d menyebut "Kartu Duplicates 1 dan Ready to Import 11" tanpa kartu lain; spec mengikuti TC.
