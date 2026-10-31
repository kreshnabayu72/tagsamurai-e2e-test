---
id: TC-GS-IMPORT-E2E-093-save-tanpa-perubahan-zero-delta-no-op-pengecualian-baris-error-sesi
title: "Save tanpa perubahan (Zero-Delta): no-op, pengecualian baris error, sesi Duplicate, kapitalisasi Employee ID"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-220
  - TC-GS-IMPORT-221
  - TC-GS-IMPORT-222
  - TC-GS-IMPORT-223
  - TC-GS-IMPORT-653
  - TC-GS-IMPORT-654
  - TC-GS-IMPORT-655
coverage:
  web: automated
---

# Save tanpa perubahan (Zero-Delta): no-op, pengecualian baris error, sesi Duplicate, kapitalisasi Employee ID

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Layanan AI: mock tetap mode normal (D-40, tabel D-41) untuk draft D-09 (badge saran AI pada baris #13); disediakan tim FE/BE.
- Data Dinamis (nama literal karena asersi bergantung pada isi dan jumlah baris; pengecualian S-12), dipulihkan oleh skrip pemulihan (Kontrak Fixture R2) sebelum tiap blok: D-01 (Draft Brand 12 baris `pending`: #1 `Acme Corp`, #2 `Lenovo`, ..., #5 `Dell`, ..., #10 `Logitech`, #11 `Cisco`, #12 `Asus`); D-09 (D-01 ditambah baris #13 `error` dengan Brand Name 121 karakter nilai sumber Brand pertama tabel D-41); D-05 (Draft User Login 8 baris `pending` dari `user-login-8.csv`, baris #1 Employee ID `EMP-1`).
- Kemampuan teknis: pengamatan toast, skrip pemulihan draft Brand (D-01, D-09) dan User Login (D-05), mock AI (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain draft Client A dan flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan draft Brand dan User Login Client A ke D-01 dan D-05.

## Test Steps

### TC-GS-IMPORT-220: Save tanpa perubahan pada baris pending

1. Klik `⋯` pada baris #1, pilih `Edit`
2. Klik `[Save]` tanpa mengubah nilai
3. Verifikasi muncul toast netral: "No changes to save."
4. Verifikasi baris #1 tetap `Acme Corp` berstatus `pending`
5. Verifikasi footer `[Import (12)]` tampil kembali (sesi tertutup)

### TC-GS-IMPORT-653: Save tanpa perubahan pada sesi Edit Baris (baris #5)

6. Tunggu toast lama hilang otomatis; klik `⋯` pada baris #5, pilih `Edit`
7. Klik `[Save]` tanpa mengubah nilai
8. Verifikasi muncul toast netral: "No changes to save."
9. Verifikasi baris #5 tetap `Dell` berstatus `pending`
10. Verifikasi footer `[Import (12)]` tampil kembali (sesi tertutup)

### TC-GS-IMPORT-654: Save tanpa perubahan pada sesi Edit this page

11. Tunggu toast lama hilang otomatis; aktifkan Switch `Edit this page`
12. Klik `[Save]` tanpa mengubah nilai
13. Verifikasi muncul toast netral: "No changes to save."
14. Verifikasi baris #1 `Acme Corp` sampai baris #10 `Logitech` tetap berstatus `pending` sebagai teks
15. Verifikasi footer `[Import (12)]` tampil kembali (sesi tertutup)

### TC-GS-IMPORT-222: Save sesi Duplicate tanpa mengubah nilai

16. Tunggu toast lama hilang otomatis; klik `⋯` pada baris #2, pilih `Duplicate`
17. Klik `[Save]` tanpa mengubah nilai
18. Verifikasi muncul toast sukses: "Success, row has been added."
19. Verifikasi toast "No changes to save." tidak tampil
20. Verifikasi draft menjadi 13 baris
21. Verifikasi salinan `Lenovo` (#3) berstatus `pending`
22. Verifikasi baris sumber `Lenovo` (#2) berstatus `duplicate`

### TC-GS-IMPORT-221: Save tanpa perubahan pada baris error

23. Tunggu toast lama hilang otomatis; pulihkan draft Brand Client A ke D-09 lewat skrip pemulihan, lalu muat ulang halaman
24. Klik tombol halaman 2 pada paginator
25. Klik `⋯` pada baris #13, pilih `Edit`
26. Klik `[Save]` tanpa mengubah nilai
27. Verifikasi toast "No changes to save." tidak tampil
28. Verifikasi sel Brand Name baris #13 berborder `danger` dengan pesan "Max. 120 characters"
29. Verifikasi baris #13 berstatus `error`
30. Verifikasi Error Summary Callout memuat baris pesan "Brand Name: Max. 120 characters" dengan badge "1 row"

### TC-GS-IMPORT-655: Save tanpa perubahan pada sesi Edit this page yang memuat baris error

31. Klik `[Cancel]` (menutup sesi Edit Baris #13 yang masih terbuka setelah Save diblokir), lalu muat ulang halaman Import > Brand
32. Klik tombol halaman 2 pada paginator
33. Aktifkan Switch `Edit this page`
34. Klik `[Save]` tanpa mengubah nilai
35. Verifikasi toast "No changes to save." tidak tampil
36. Verifikasi sel Brand Name baris #13 berborder `danger` dengan pesan "Max. 120 characters"
37. Verifikasi baris #13 berstatus `error`
38. Verifikasi baris #11 `Cisco` berstatus `pending`
39. Verifikasi baris #12 `Asus` berstatus `pending`

### TC-GS-IMPORT-223: Perubahan kapitalisasi Employee ID

40. Klik `[Cancel]` (menutup sesi Edit this page yang masih terbuka), pulihkan draft User Login Client A ke D-05 lewat skrip pemulihan, pilih Sub-Tab User Login, lalu muat ulang halaman
41. Klik `⋯` pada baris #1 (Employee ID `EMP-1`), pilih `Edit`
42. Ubah Employee ID baris #1 dari `EMP-1` menjadi `emp-1`
43. Klik `[Save]`
44. Verifikasi muncul toast sukses: "Success, row has been updated."
45. Verifikasi toast "No changes to save." tidak tampil
46. Verifikasi baris #1 menampilkan Employee ID `emp-1`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-653 dan TC-654 sebelum TC-222 (TC-222 menambah baris draft), TC-221 dan TC-655 (D-09) sesudahnya, TC-223 (Sub-Tab User Login) paling akhir.
- Langkah penghubung (tanpa `Verifikasi`): langkah 6, 11, 16, 23 (menunggu toast, pemulihan draft, muat ulang) menjalankan Precondition draft; langkah 31 dan 40 menutup sesi edit yang tetap terbuka karena Save diblokir pada TC-221 dan TC-655 (Zero-Delta tidak berlaku untuk baris error). Pada langkah 11 draft D-01 tidak dipulihkan karena TC-220 dan TC-653 tidak mengubah draft.
- Asersi tidak tampil (langkah 19, 27, 35, 45) diletakkan segera setelah Save dan sebelum asersi artefak; klik `[Save]` menjadi anchor positif yang buktinya menyusul pada `Verifikasi` hasil (butir 11 bagian 8b).
- Spec berisi 46 langkah. Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional) dan satu topik (Zero-Delta), tiap blok membuka sesi sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-GS-IMPORT-209 sampai 217 dan 652 (Save berhasil) ada di spec 092.
- Temuan untuk QA:
  - TC-GS-IMPORT-221 dan 655 Expected a ("Toast 'No changes to save.' tidak tampil") tidak menyebut toast pengganti (Save diblokir); spec hanya mengasersi toast tidak tampil.
  - TC-GS-IMPORT-222 Post Condition tidak ada; Expected b-c diasersi. TC-GS-IMPORT-220 dan 653 Post Condition tidak ada.
  - Mekanisme skrip pemulihan draft D-01, D-05, D-09 (Kontrak Fixture R2) tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
