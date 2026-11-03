---
id: TC-FA-LBL-E2E-052-dialog-d-02-label-dipakai-atau-default-label-hitungan-jamak-tunggal-status-aset-bagian-2-2
title: "Dialog D-02 Label Dipakai atau Default Label (Hitungan Jamak/Tunggal, Status Aset) (bagian 2/2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-166
  - TC-FA-LBL-169
  - TC-FA-LBL-186
  - TC-FA-LBL-195
coverage:
  web: automated
---

# Dialog D-02 Label Dipakai atau Default Label (Hitungan Jamak/Tunggal, Status Aset) (bagian 2/2)

## Prerequisites

- Mode: FE+BE. Backend nyata pada Company Alpha; tidak ada respons yang di-mock atau di-intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.assetLabeling.totalControl.email`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. `fixtures/asset-labeling.json` belum ada dan disediakan tim FE.
- Hook suite `before`, `beforeEach`, dan `after` (lihat `suite.md`) berlaku. Seeding label di hook `before` spec ini lewat fixture BE; cleanup di hook `after` menghapus label sisa milik spec dan tidak mengasumsikan setup berhasil penuh.
- Data Pre-setup (hanya dibaca, tidak diubah; dialog hanya ditutup dengan `[OK]`, Esc, atau backdrop sehingga Last Updated label tidak berubah, S-06): katalog Company Alpha 9 label (#12): `Finance Department` (Total Asset 5; 6 relasi, aset Deleted `Scanner Zebra - 6` tidak dihitung), `High Priority` (Total Asset 3), `Warehouse Priority` (Default Label Asset Name `Warehouse Item`); aset berlabel (#13) dan Asset Name (#14).
- Data Dinamis: tidak ada.
- Katalog Company Alpha berisi 9 label Pre-setup #12 dan tidak ada label seed; seluruhnya tampil di satu halaman (page size 10).
- Kemampuan teknis: tidak ada selain login dan seeding Pre-setup.
- State global: tidak ada yang diubah, tidak ada cleanup.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LBL-166: Hitungan D-02 menghitung aset Draft, Waiting for Approval, Active, Disposed dan mengabaikan Deleted

1. Klik `⋯` pada baris `Finance Department` lalu klik `Delete`
2. Verifikasi dialog Title `Cannot Delete Label` tampil dan menggantikan dialog konfirmasi (dialog D-01 tidak muncul)
3. Verifikasi body bullet `• Finance Department`
4. Verifikasi baris `This label is assigned to 5 assets.` (6 relasi: 1 aset Deleted tidak dihitung)
5. Verifikasi kalimat penutup `Remove it from those assets and Default Label lists before deleting it.`
6. Verifikasi footer hanya satu tombol `[OK]` (Button Text, Contrast); tidak ada tombol `[Delete]`
7. Klik `[OK]`
8. Verifikasi total Asset pada baris `Finance Department` di Labels List bernilai `5`
9. Klik `⋯` pada baris `Finance Department` lalu klik `Detail`
10. Verifikasi Drawer Tagged Asset memuat 5 baris
11. Tutup Drawer Tagged Asset

### TC-FA-LBL-169: Dialog D-02 tidak menutup saat backdrop diklik dan Esc setara OK

12. Klik `⋯` pada baris `High Priority` lalu klik `Delete`
13. Klik area gelap di luar dialog
14. Verifikasi klik backdrop tidak menutup dialog
15. Tekan Esc
16. Verifikasi Esc menutup dialog
17. Verifikasi tanpa mutasi: baris `High Priority` tetap ada dengan Total Asset `3`

### TC-FA-LBL-186: Bulk dengan 1 baris terpilih yang dipakai memakai dialog single D-02

18. Centang baris `High Priority`
19. Klik `Bulk Action` lalu klik `Delete`
20. Verifikasi dialog Title `Cannot Delete Label` (singular, bukan `Cannot Delete Labels`)
21. Verifikasi baris `This label is assigned to 3 assets.`
22. Verifikasi footer hanya satu tombol `[OK]`
23. Klik `[OK]`
24. Klik ikon `×`

### TC-FA-LBL-195: Screening dialog Bulk Delete semua dipakai (D-05) dan OK tanpa mutasi

25. Centang `High Priority` dan `Warehouse Priority`
26. Klik `Bulk Action` lalu klik `Delete`
27. Verifikasi dialog Title `Cannot Delete Labels`, bullet `• High Priority` dan `• Warehouse Priority`, teks `These labels are in use and cannot be deleted.`, satu tombol `[OK]` (Button Text, Contrast)
28. Klik `[OK]`
29. Verifikasi dialog tertutup
30. Verifikasi tidak ada toast
31. Verifikasi seleksi tidak berubah: counter `2 Labels selected`
32. Klik ikon `×`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): klik `[OK]` menutup dialog sebelum TC berikutnya (S-09); langkah 11 menutup Drawer Tagged Asset sesudah hitungan diverifikasi; langkah 24 dan langkah 32 membersihkan seleksi (S-09). Search tidak dipakai karena seluruh 9 label Pre-setup #12 tampil di satu halaman.
- Verifikasi langkah 8 dan langkah 10 berasal dari Expected f TC-FA-LBL-166 (hitungan `5` sama dengan Total Asset di Labels List dan jumlah baris di Drawer Tagged Asset); Langkah Uji TC tidak memberi langkahnya sehingga membuka Drawer lewat row action `Detail` (NC-02) ditulis sebagai langkah penghubung.
- Pembagian TC lintas spec: TC-FA-LBL-162 sampai TC-FA-LBL-165 ada di spec 051; TC-FA-LBL-168 (OK pada D-02 tanpa mutasi dan tanpa log) ada di spec Absence Log suite ini karena Expected-nya memuat absence log (S-05). TC-FA-LBL-186 (D-02 lewat Bulk Action satu baris) dan TC-FA-LBL-195 (D-05, bentuk jamak dialog yang sama) ada di spec ini; TC-FA-LBL-191 sampai TC-FA-LBL-194 ada di spec 056.
- Pencatatan log: asersi absence log tidak ada di spec ini (S-05). Post Condition TC-FA-LBL-195 ("tidak ada mutasi dan tidak ada entri log") tidak punya langkah observasi di TC dan tidak diasersi.
- Temuan untuk QA:
  - Expected f TC-FA-LBL-166 tidak punya langkah di Langkah Uji (cara membaca Total Asset dan jumlah baris Drawer); spec menambahkan langkah penghubung.
  - Post Condition TC-FA-LBL-195 (tanpa mutasi, tanpa entri log) tidak diasersi karena TC tidak memberi langkah observasi.
  - Expected TC-FA-LBL-169 b ("Esc menutup dialog tanpa mutasi") tidak menyebut cara mengamati mutasi; spec mengamati baris `High Priority` dan Total Asset-nya.
