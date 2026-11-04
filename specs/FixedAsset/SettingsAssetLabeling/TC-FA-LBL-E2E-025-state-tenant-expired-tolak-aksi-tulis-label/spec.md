---
id: TC-FA-LBL-E2E-025-state-tenant-expired-tolak-aksi-tulis-label
title: "State tenant Expired: Create, Edit, Delete, dan Bulk Delete label ditolak"
priority: Critical
caseType: Negative
status: draft
sourceRules:
  - E-FALB-16
  - F-FALB-02.k6
  - F-FALB-03.k7
  - F-FALB-04.k6
  - F-FALB-05.k5
  - F-FALB-10.k2
coverage:
  web: automated
---

# State tenant Expired: Create, Edit, Delete, dan Bulk Delete label ditolak

## Prerequisites

- Mode: FE+BE
- Akun Total Control client Expired `DU-34` (env `FA_EXP_TC_EMAIL`, `FA_EXP_TC_PASSWORD`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` spec ini mengembalikan sesi ke akun default suite.
- Data uji: `DU-52` (label pre-setup client Expired: tepat 1 label, bersih, satu-satunya baris Labels List, Total Asset 0 dan bukan Default Label; hanya dibaca, tidak diubah oleh spec). Nilai input aksi tulis yang ditolak memakai nilai turunan `DU-52`: akhiran `-baru` untuk Label Name Create dan akhiran `-ubah` untuk Label Name Edit.
- Kemampuan teknis: kemampuan baca BE untuk jumlah entri Changelog, System Log, dan Activity Log, dan fixture BE untuk membaca label (keduanya disediakan tim FE/BE).
- State global: client Expired disediakan sebagai pre-setup dan spec tidak mengubah status client; tidak ada data yang dibuat spec.

## Test Steps

### E-FALB-16: Create, Edit, Delete, dan Bulk Delete ditolak saat client Expired

1. Catat baseline jumlah entri Changelog, System Log, dan Activity Log client ini lewat kemampuan baca BE.
2. Ketik Search `DU-52`, tekan Enter.
3. Klik `[+ Label]`.
4. Ketik Label Name `DU-52` berakhiran `-baru`.
5. Klik `[Submit]`.
6. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil.
7. Verifikasi modal Create Label tertutup.
8. Verifikasi tabel Labels List menampilkan baris Label `DU-52` dengan nama semula dan tidak memuat baris `DU-52` berakhiran `-baru`.
9. Tunggu toast lama hilang otomatis.
10. Klik `[⋯]` pada baris Label `DU-52`, pilih `Edit`.
11. Ganti isi Label Name dengan `DU-52` berakhiran `-ubah`.
12. Klik `[Save]`.
13. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil.
14. Verifikasi modal Edit Label tertutup.
15. Verifikasi tabel Labels List menampilkan baris Label `DU-52` dengan nama semula (bukan `DU-52` berakhiran `-ubah`).
16. Tunggu toast lama hilang otomatis.
17. Klik `[⋯]` pada baris Label `DU-52`, pilih `Delete`.
18. Klik `[Delete]` pada dialog konfirmasi.
19. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil.
20. Verifikasi dialog konfirmasi Delete tertutup.
21. Verifikasi tabel Labels List masih menampilkan baris Label `DU-52`.
22. Tunggu toast lama hilang otomatis.
23. Centang checkbox pada baris Label `DU-52`.
24. Klik `Bulk Action`, pilih `Delete`.
25. Klik `[Delete]` pada dialog konfirmasi.
26. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil.
27. Verifikasi dialog konfirmasi Bulk Delete tertutup.
28. Verifikasi tabel Labels List masih menampilkan baris Label `DU-52`.
29. Verifikasi lewat fixture BE jumlah label client ini dan nama serta warna label `DU-52` sama dengan keadaan semula (tidak ada perubahan data).
30. Verifikasi lewat kemampuan baca BE tidak ada entri log baru: selisih jumlah entri Changelog, System Log, dan Activity Log terhadap baseline langkah 1 sama dengan 0.

### F-FALB-02.k6: Create ditolak saat client Expired

31. Verifikasi lewat fixture BE tidak ada label bernama `DU-52` berakhiran `-baru`.

### F-FALB-03.k7: Edit ditolak saat client Expired

32. Verifikasi lewat fixture BE nama label `DU-52` tidak berakhiran `-ubah`.

### F-FALB-04.k6: Delete ditolak saat client Expired

33. Verifikasi lewat fixture BE label `DU-52` masih ada di katalog.

### F-FALB-05.k5: Bulk Delete ditolak saat client Expired

34. Verifikasi tabel Labels List masih menampilkan baris Label `DU-52`.

### F-FALB-10.k2: Penolakan karena client Expired menulis nol entri log

35. Verifikasi lewat kemampuan baca BE selisih jumlah entri Changelog sama dengan 0, selisih jumlah entri System Log sama dengan 0, dan selisih jumlah entri Activity Log sama dengan 0 terhadap baseline langkah 1.

## Notes

- Pembagian klausa lintas spec: klausa tiap aturan untuk client Suspended diasersi di spec 014 dengan langkah yang sama; spec ini hanya client Expired. `F-FALB-10.k2` juga dikutip spec 014 (client Suspended), 015 dan 027 (batas katalog), 017 (guard Default Label dan guard saat konfirmasi), dan 018 (label dipakai 500 aset), yang masing-masing mengasersi kasus penolakannya sendiri.
- Pengecualian S-05 (kelas h, prinsip 13g): aturan state tenant yang objek ujinya penolakan aksi tulis mengasersi "tidak ada entri log baru" di spec ini dengan `Verifikasi` selisih jumlah entri terhadap baseline per surface log (langkah 30 dan 35).
- Langkah penghubung (S-03): langkah 2 (Search untuk menemukan baris target, R-16), 9, 16, 22 (menunggu toast sebelumnya hilang otomatis sebelum asersi toast berikutnya, R-12), 23 sampai 25 (seleksi satu baris pada Bulk Action Bar diperlakukan sebagai Delete tunggal menurut PRD §3.4; data uji `DU-52` memuat satu label per client).
- Pemuatan ulang tabel pada klausa `E-FALB-16` ("tabel di-refresh") diamati lewat isi tabel sesudah tiap penolakan: langkah 8, 15, 21, dan 28 (baris `DU-52` tetap tampil dengan nama semula), dan langkah 34 di bawah `F-FALB-05.k5`.
- Baseline log (langkah 1) dicatat sebelum aksi pemicu pertama; langkah 30 dan 35 membaca jumlah entri sesudah keempat aksi ditolak.
- Klausa nol entri log milik baris `F-FALB-02.k6`, `F-FALB-03.k7`, `F-FALB-04.k6`, dan `F-FALB-05.k5` (Aksi/Log: nol entri log) dipenuhi pada langkah 30 dan 35: selisih jumlah entri Changelog, System Log, dan Activity Log terhadap baseline langkah 1 sama dengan 0, dibaca sesudah keempat aksi ditolak; langkah 35 berada di bawah `F-FALB-10.k2`.
