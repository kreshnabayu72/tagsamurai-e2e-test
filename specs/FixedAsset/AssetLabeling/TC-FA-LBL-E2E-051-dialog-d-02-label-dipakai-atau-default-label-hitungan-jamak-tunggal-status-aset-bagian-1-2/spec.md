---
id: TC-FA-LBL-E2E-051-dialog-d-02-label-dipakai-atau-default-label-hitungan-jamak-tunggal-status-aset-bagian-1-2
title: "Dialog D-02 Label Dipakai atau Default Label (Hitungan Jamak/Tunggal, Status Aset) (bagian 1/2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-162
  - TC-FA-LBL-163
  - TC-FA-LBL-164
  - TC-FA-LBL-165
coverage:
  web: automated
---

# Dialog D-02 Label Dipakai atau Default Label (Hitungan Jamak/Tunggal, Status Aset) (bagian 1/2)

## Prerequisites

- Mode: FE+BE. Backend nyata pada Company Alpha; tidak ada respons yang di-mock atau di-intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.assetLabeling.totalControl.email`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. `fixtures/asset-labeling.json` belum ada dan disediakan tim FE.
- Hook suite `before`, `beforeEach`, dan `after` (lihat `suite.md`) berlaku. Seeding label di hook `before` spec ini lewat fixture BE; cleanup di hook `after` menghapus label sisa milik spec dan tidak mengasumsikan setup berhasil penuh.
- Data Pre-setup (hanya dibaca, tidak diubah; dialog hanya ditutup dengan `[OK]` sehingga Last Updated label tidak berubah, S-06): katalog Company Alpha 9 label (#12): `High Priority` (Total Asset 3), `Executive Asset` (Total Asset 1), `Warehouse Priority` (Total Asset 0, Default Label Asset Name `Warehouse Item`), `Field Kit` (Total Asset 2, Default Label Asset Name `Handheld Scanner` dan `Barcode Reader`); aset berlabel (#13) dan Asset Name (#14).
- Data Dinamis: tidak ada.
- Katalog Company Alpha berisi 9 label Pre-setup #12 dan tidak ada label seed; seluruhnya tampil di satu halaman (page size 10).
- Kemampuan teknis: tidak ada selain login dan seeding Pre-setup.
- State global: tidak ada yang diubah, tidak ada cleanup.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LBL-162: Delete label yang dipakai banyak aset menampilkan D-02 dengan hitungan jamak

1. Klik `⋯` pada baris `High Priority` lalu klik `Delete`
2. Verifikasi dialog Title `Cannot Delete Label` tampil dan menggantikan dialog konfirmasi (dialog D-01 tidak muncul)
3. Verifikasi body bullet `• High Priority`
4. Verifikasi baris `This label is assigned to 3 assets.`
5. Verifikasi baris Default Label tidak tampil
6. Verifikasi kalimat penutup `Remove it from those assets and Default Label lists before deleting it.`
7. Verifikasi footer hanya satu tombol `[OK]` (Button Text, Contrast); tidak ada tombol `[Delete]`
8. Klik `[OK]`

### TC-FA-LBL-163: Delete label yang dipakai satu aset menampilkan hitungan tunggal

9. Klik `⋯` pada baris `Executive Asset` lalu klik `Delete`
10. Verifikasi dialog Title `Cannot Delete Label` tampil dan menggantikan dialog konfirmasi (dialog D-01 tidak muncul)
11. Verifikasi body bullet `• Executive Asset`
12. Verifikasi baris `This label is assigned to 1 asset.`
13. Verifikasi baris Default Label tidak tampil
14. Verifikasi kalimat penutup `Remove it from those assets and Default Label lists before deleting it.`
15. Verifikasi footer hanya satu tombol `[OK]` (Button Text, Contrast); tidak ada tombol `[Delete]`
16. Klik `[OK]`

### TC-FA-LBL-164: Delete label yang hanya menjadi Default Label satu Asset Name menampilkan D-02

17. Klik `⋯` pada baris `Warehouse Priority` lalu klik `Delete`
18. Verifikasi dialog Title `Cannot Delete Label` tampil dan menggantikan dialog konfirmasi (dialog D-01 tidak muncul)
19. Verifikasi body bullet `• Warehouse Priority`
20. Verifikasi baris `This label is used as Default Label by 1 asset name.`
21. Verifikasi baris jumlah aset tidak tampil
22. Verifikasi kalimat penutup `Remove it from those assets and Default Label lists before deleting it.`
23. Verifikasi footer hanya satu tombol `[OK]` (Button Text, Contrast); tidak ada tombol `[Delete]`
24. Klik `[OK]`

### TC-FA-LBL-165: Delete label yang dipakai aset dan menjadi Default Label dua Asset Name

25. Klik `⋯` pada baris `Field Kit` lalu klik `Delete`
26. Verifikasi dialog Title `Cannot Delete Label` tampil dan menggantikan dialog konfirmasi (dialog D-01 tidak muncul)
27. Verifikasi body bullet `• Field Kit`
28. Verifikasi baris `This label is assigned to 2 assets.` diikuti baris `This label is used as Default Label by 2 asset names.`
29. Verifikasi kalimat penutup `Remove it from those assets and Default Label lists before deleting it.`
30. Verifikasi footer hanya satu tombol `[OK]` (Button Text, Contrast); tidak ada tombol `[Delete]`
31. Klik `[OK]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): klik `[OK]` di akhir tiap TC menutup dialog sebelum TC berikutnya (S-09). Search tidak dipakai karena seluruh 9 label Pre-setup #12 tampil di satu halaman.
- Pembagian TC lintas spec: TC-FA-LBL-166, TC-FA-LBL-169, TC-FA-LBL-186, dan TC-FA-LBL-195 (D-02 dan D-05 lanjutan) ada di spec 052; TC-FA-LBL-168 (OK pada D-02 tanpa mutasi dan tanpa log) ada di spec Absence Log suite ini karena Expected-nya memuat absence log (S-05).
- Pencatatan log: asersi absence log tidak ada di spec ini (S-05). Post Condition TC-FA-LBL-162 sampai TC-FA-LBL-165 ("tidak ada mutasi dan tidak ada entri log baru") tidak punya langkah observasi di TC dan tidak diasersi.
- Temuan untuk QA:
  - Post Condition TC-FA-LBL-162 sampai TC-FA-LBL-165 (tanpa mutasi, tanpa entri log) tidak diasersi karena TC tidak memberi langkah observasi.
  - Expected c TC-FA-LBL-162 sampai TC-FA-LBL-164 menyebut baris yang tidak tampil "karena hitungan 0"; hitungan 0 tidak teramati terpisah di UI sehingga spec hanya mengasersi barisnya tidak tampil.
