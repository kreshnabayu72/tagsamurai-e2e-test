---
id: TC-FA-FAAC-E2E-177-state-tenant-write-lockdown-suspended-expired
title: "State Tenant: Aksi Tulis Create, Edit, Toggle Active, dan Delete Ditolak saat Client Suspended atau Expired"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-590
  - TC-FA-FAAC-591
  - TC-FA-FAAC-592
  - TC-FA-FAAC-593
coverage:
  web: automated
---

# State Tenant: Aksi Tulis Create, Edit, Toggle Active, dan Delete Ditolak saat Client Suspended atau Expired

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- State global yang diubah spec: status client (`Active`, `Suspended`, `Expired`). Pelaku perubahan status tidak disebut TC, PRD, atau LLD; fixture BE untuk mengubah status entitas "disediakan tim FE/BE" (tanpa akun atau endpoint karangan). Status awal `Active` dicatat di hook `before`; hook `after` memulihkan status ke `Active` walau spec gagal di tengah (langkah 32 hanya pemulihan eksplisit). Dampak sampingan: Last Updated client tidak dijamin kembali.
- Data seed Asset Class (kode literal TC, disediakan fixture BE, milik spec ini, dibuat ulang bila berubah): `B-ANCHOR` (Active, tanpa Asset Name ter-assign; target Save yang ditolak), `B-FREE14` (Active, tanpa Asset Name), `B-DEL5` (tanpa Asset Name).
- Data Dinamis: Class Code literal `B-LCK` dan Class Name `Lockdown Create {runId}-177` pada form Create yang ditolak (tidak pernah tersimpan; fixture BE menghapus sisa `B-LCK` di hook `before` dan `after` bila ternyata tersimpan).
- Nilai form Create valid (TC-590 menulis "form valid" tanpa nilai; dipakai set Data Uji valid TC-FA-FAAC-262): Class Code `B-LCK`; Class Name `Lockdown Create {runId}-177`; Method `Straight Line`; Useful Life `96`; Depreciation Start Convention `Full month from in-service date`; Tax Depreciation Class `Bukan bangunan – Kelompok 2`; Tax Method `Declining Balance`; Tax Depreciation Start Rule `Month of expenditure`. Nilai Class Name pengganti untuk Edit: `Lockdown Rename`.
- Kemampuan teknis: pembacaan jumlah Asset Class, Class Name `B-ANCHOR`, dan jumlah entri Changelog Asset Class, System Log, dan Activity Log lewat kemampuan baca BE (disediakan tim FE/BE; audit trail permanen, asersi log memakai selisih terhadap baseline, bukan angka absolut).
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

1. Atur lewat fixture BE status client menjadi `Suspended`, lalu muat ulang halaman

### TC-FA-FAAC-590: Submit Create saat entitas Suspended ditolak

2. Catat baseline lewat kemampuan baca BE: jumlah Asset Class, jumlah entri Changelog Asset Class, System Log, dan Activity Log
3. Klik tombol `+ Asset Class`, lalu isi form dengan nilai valid (Class Code `B-LCK`, Class Name `Lockdown Create {runId}-177`)
4. Klik `Submit`
5. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.`
6. Verifikasi tidak ada Asset Class dibuat: jumlah Asset Class sama dengan baseline
7. Verifikasi jumlah entri Changelog Asset Class, System Log, dan Activity Log sama dengan baseline (tidak ada log)
8. Klik breadcrumb `Asset Class`
9. Verifikasi dialog `Unsaved Changes` tampil
10. Klik `[Leave]`

### TC-FA-FAAC-592: Toggle Active saat entitas Suspended ditolak

11. Ketik Search `B-FREE14`, tekan Enter
12. Klik toggle kolom Active pada baris `B-FREE14` (On), lalu klik `Deactivate` pada dialog konfirmasi
13. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.`
14. Verifikasi toggle kolom Active baris `B-FREE14` kembali ke nilai tersimpan (On)

### TC-FA-FAAC-593: Delete saat entitas Suspended ditolak

15. Ganti isi kotak search dengan `B-DEL5`, tekan Enter
16. Klik ikon `⋯` pada baris `B-DEL5`, pilih `Delete`, lalu klik `Delete` pada dialog konfirmasi
17. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.`
18. Verifikasi baris `B-DEL5` tetap ada di tabel
19. Klik `(←)` pada kotak Search
20. Atur lewat fixture BE status client menjadi `Expired`, lalu muat ulang halaman

### TC-FA-FAAC-591: Save Edit saat entitas Expired ditolak

21. Catat baseline lewat kemampuan baca BE: Class Name `B-ANCHOR`, jumlah entri Changelog Asset Class, System Log, dan Activity Log
22. Ketik Search `B-ANCHOR`, tekan Enter
23. Klik link Class Code `B-ANCHOR` di tabel
24. Ubah Class Name menjadi `Lockdown Rename`
25. Klik `Save`
26. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.`
27. Verifikasi tidak ada data berubah: Class Name `B-ANCHOR` sama dengan baseline
28. Verifikasi jumlah entri Changelog Asset Class, System Log, dan Activity Log sama dengan baseline (tidak ada log)
29. Kembalikan Class Name ke nilai tersimpan
30. Klik breadcrumb `Asset Class`
31. Klik `(←)` pada kotak Search
32. Atur lewat fixture BE status client kembali menjadi `Active`, lalu muat ulang halaman

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC diubah dari urutan nomor (590, 592, 593 lalu 591) supaya status client hanya berganti `Suspended` ke `Expired` satu kali; tiap TC tetap memakai data dan baseline sendiri (S-10).
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 20, dan 32 (mengganti status client); langkah 8 sampai 10 (menutup form Create yang dirty lewat breadcrumb, S-08; `Verifikasi` dialog `Unsaved Changes` diwajibkan S-08); langkah 11, 15, 22 (Search untuk menemukan baris target, R-16); langkah 19 dan 31 (mengosongkan Search); langkah 29 dan 30 (mengembalikan field ke nilai tersimpan sebelum meninggalkan Detail, S-09).
3. S-05 dan prinsip 13g (pengecualian kelas h): klausa "tidak ada log" pada TC-590 dan TC-591 diasersi di spec ini dengan selisih jumlah entri terhadap baseline per surface log (Changelog Asset Class, System Log, Activity Log); baseline dicatat sebelum pemicu tiap TC (S-12). TC-592 dan TC-593 tidak menyebut log pada Expected-nya, sehingga tidak ada asersi log untuk keduanya.
4. Pengecualian kode seed literal (S-06/S-12): TC mewajibkan baris `B-FREE14`, `B-DEL5`, dan `B-ANCHOR`; kode dipakai apa adanya tanpa suffix `{runId}`. Target aksi tulis hanya ditolak server (tidak berubah); seed milik spec dan dibuat ulang fixture BE di hook `after` bila berubah.
5. Temuan untuk QA: TC-590 menulis "isi form valid" tanpa nilai; spec memakai nilai valid dari Data Uji TC-262. TC-592 menulis "lalu konfirmasi" tanpa label tombol dialog; spec memakai `Deactivate` karena `B-FREE14` Active. TC-591 dan TC-593 tidak menyebut label tombol dialog dan toast sukses sebagai anchor; spec memakai toast error server sebagai anchor absence (8b butir 2).
6. Class Code `B-LCK` ditulis literal dan `{runId}-177` dipindah ke Class Name karena Class Code dibatasi 15 karakter sehingga `B-LCK{runId}-177` tidak muat (S-12, nama literal; pola spec 066 sampai 069; kode berbeda antar spec); form Create ini ditolak server sehingga tidak ada data tersimpan, dan fixture BE menghapus sisa `B-LCK` di hook `before` dan `after`.
