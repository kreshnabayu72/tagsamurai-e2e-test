---
id: TC-FA-FAAC-E2E-183-resilience-create-edit-duplicate
title: "Resilience: Submit Create, Save Edit, dan Submit Duplicate Gagal karena Error Server 5xx Mempertahankan Form"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-143
  - TC-FA-FAAC-180
  - TC-FA-FAAC-269
coverage:
  web: automated
---

# Resilience: Submit Create, Save Edit, dan Submit Duplicate Gagal karena Error Server 5xx Mempertahankan Form

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata)
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Kemampuan teknis: `Spectra.intercept` parsial yang memaksa respons HTTP 5xx pada permintaan Create, Edit, dan Create hasil Duplicate di atas backend nyata; intercept dilepas segera sesudah submit (S-09). Endpoint permintaan tidak didefinisikan di TC, PRD, atau LLD yang dibaca, sehingga dipilih tim FE saat script. Pembacaan jumlah Asset Class, Class Name `B-SHARE`, dan jumlah entri Changelog Asset Class, System Log, dan Activity Log lewat kemampuan baca BE (disediakan tim FE/BE; audit trail permanen, asersi log memakai selisih terhadap baseline, bukan angka absolut).
- Data seed (kode literal TC, disediakan fixture BE, dibaca, tidak diubah karena semua submit gagal): Asset Class `B-SHARE` dan `B-ANCHOR` (Active). Kode `B-5XX` dan `B-DUP5` tidak ada; hook `after` menghapusnya lewat fixture BE bila ternyata tersimpan.
- Nilai form Create valid TC-143 (TC menulis "semua field valid" tanpa nilai; dipakai set Data Uji valid TC-FA-FAAC-262): Class Code `B-5XX`; Class Name `Resilience Create`; Method `Straight Line`; Useful Life `96`; Depreciation Start Convention `Full month from in-service date`; Tax Depreciation Class `Bukan bangunan – Kelompok 2`; Tax Method `Declining Balance`; Tax Depreciation Start Rule `Month of expenditure`. Nilai Class Name pengganti untuk Edit TC-180: `Fail Rename`. Class Code Duplicate TC-269: `B-DUP5`.
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-143: Submit gagal karena server error 5xx mempertahankan form

1. Catat baseline lewat kemampuan baca BE: jumlah Asset Class dan jumlah entri Changelog Asset Class, System Log, dan Activity Log
2. Klik tombol `+ Asset Class` di toolbar tabel
3. Isi semua field valid (Class Code `B-5XX`)
4. Pasang intercept respons 5xx pada permintaan Create
5. Klik `Submit`
6. Lepas intercept respons 5xx
7. Verifikasi toast error `Error, failed to create asset class.`
8. Verifikasi Halaman Detail tetap terbuka mode Create dengan semua isian dipertahankan
9. Verifikasi tombol `Submit` kembali aktif untuk dicoba ulang
10. Verifikasi tidak ada Asset Class `B-5XX` dibuat: jumlah Asset Class sama dengan baseline
11. Verifikasi jumlah entri Changelog Asset Class, System Log, dan Activity Log sama dengan baseline (tidak ada log)
12. Klik breadcrumb `Asset Class`
13. Verifikasi dialog `Unsaved Changes` tampil
14. Klik `[Leave]`

### TC-FA-FAAC-180: Save gagal karena server error 5xx mempertahankan halaman Detail

15. Catat baseline lewat kemampuan baca BE: Class Name `B-SHARE` dan jumlah entri Changelog Asset Class, System Log, dan Activity Log
16. Ketik Search `B-SHARE`, tekan Enter
17. Klik link Class Code `B-SHARE` di tabel
18. Ubah Class Name menjadi `Fail Rename`
19. Pasang intercept respons 5xx pada permintaan Edit
20. Klik `Save`
21. Lepas intercept respons 5xx
22. Verifikasi toast error `Error, failed to update asset class.`
23. Verifikasi Halaman Detail tetap terbuka dengan isian utuh
24. Verifikasi tombol `Save` kembali aktif
25. Verifikasi jumlah entri Changelog Asset Class, System Log, dan Activity Log sama dengan baseline (tidak ada log)
26. Kembalikan Class Name ke nilai tersimpan
27. Klik breadcrumb `Asset Class`
28. Verifikasi Class Name baris `B-SHARE` di tabel sama dengan nilai baseline (tidak berubah)

### TC-FA-FAAC-269: Submit hasil Duplicate gagal 5xx

29. Catat baseline lewat kemampuan baca BE: jumlah Asset Class
30. Ganti isi kotak search dengan `B-ANCHOR`, tekan Enter
31. Klik ikon `⋯` pada baris `B-ANCHOR` lalu pilih `Duplicate`
32. Isi Class Code `B-DUP5`
33. Pasang intercept respons 5xx pada permintaan Create hasil Duplicate
34. Klik `Submit`
35. Lepas intercept respons 5xx
36. Verifikasi toast error `Error, failed to create asset class.`
37. Verifikasi halaman tetap terbuka dengan isian utuh
38. Verifikasi tidak ada Asset Class dibuat: jumlah Asset Class sama dengan baseline
39. Klik breadcrumb `Asset Class`
40. Verifikasi dialog `Unsaved Changes` tampil
41. Klik `[Leave]`
42. Klik `(←)` pada kotak Search

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 12 sampai 14 dan 39 sampai 41 (menutup form yang dirty lewat breadcrumb, S-08; `Verifikasi` dialog `Unsaved Changes` diwajibkan S-08); langkah 16 dan 30 (Search untuk menemukan baris target, R-16); langkah 26 dan 27 (mengembalikan field ke nilai tersimpan sebelum meninggalkan Detail, S-09); langkah 42 (mengosongkan Search). Intercept dilepas segera sesudah submit (langkah 6, 21, 35; S-09).
3. Prinsip 13g dan S-12: klausa "tidak ada log" pada TC-143 dan TC-180 adalah asersi jumlah pada TC fungsional (aksi UI dengan kegagalan server yang dipaksa, kelas b; bukan request langsung yang ditolak server) sehingga diasersi di spec ini dengan `Verifikasi` selisih jumlah entri terhadap baseline per surface log (Changelog Asset Class, System Log, Activity Log), sesudah toast error server sebagai anchor positif; baseline dicatat sebelum pemicu tiap TC.
4. Pengecualian kode seed literal (S-06/S-12): TC mewajibkan `B-SHARE`, `B-ANCHOR`, `B-5XX`, dan `B-DUP5`; nilai dipakai apa adanya tanpa suffix `{runId}`. Semua submit gagal sehingga data tidak berubah.
5. Alasan di atas sekitar 35 langkah: ketiga blok satu kelas harness (b), berdiri sendiri dengan baseline sendiri, dan tidak mengubah data; konvensi bagian 3 prinsip 13 menetapkan kelas ringan cukup satu spec per kelas per modul, bukan per aksi, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
6. Temuan untuk QA: TC-143 dan TC-180 tidak menyebut nilai semua field valid dan nilai awal `B-SHARE`; TC-143 memuat klausa "tidak ada log" sebagai bagian butir Expected b dan TC-269 tidak menyebut log. Spec mengikuti TC. Dua TC lain kelas b pada pembuatan (TC-262 dan TC-292) ada di spec resilience submit draft dan Use Recommended Classes suite ini.
