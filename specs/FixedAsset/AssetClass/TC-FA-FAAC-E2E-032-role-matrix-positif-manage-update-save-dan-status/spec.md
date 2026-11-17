---
id: TC-FA-FAAC-E2E-032-role-matrix-positif-manage-update-save-dan-status
title: "Role Matrix Positif: Manage Accounting (Read, Update) Save Edit, Activate, Deactivate, dan Bulk Deactivate Berhasil"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-78
  - TC-FA-FAAC-79
  - TC-FA-FAAC-80
  - TC-FA-FAAC-81
sourceRules: ["T-02", "F-FAAC-02.k18", "§4.1.1#r3", "FAAC-LOGIC-10b", "D-08", "T-04", "§[F-FAAC-03] Activate Asset Class#b2", "D-01", "T-05a", "§[F-FAAC-04] Deactivate Asset Class#b4", "D-02"]
smoke: []
dependsOn: []
trace:
  "T-02": 5
  "F-FAAC-02.k18": 6
  "§4.1.1#r3": 7
  "FAAC-LOGIC-10b": 7
  "D-08": 10
  "T-04": 12
  "§[F-FAAC-03] Activate Asset Class#b2": 13
  "D-01": 16
  "T-05a": [18, 28]
  "§[F-FAAC-04] Deactivate Asset Class#b4": 19
  "D-02": 26
coverage:
  web: automated
---

# Role Matrix Positif: Manage Accounting (Read, Update) Save Edit, Activate, Deactivate, dan Bulk Deactivate Berhasil

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Manage accounting (Read, Update)) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Role yang diuji (tiap role memakai akunnya sendiri):

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Manage accounting (Read, Update) | `manageAccountingReadUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_RU_PASSWORD` | TC-FA-FAAC-78, TC-FA-FAAC-79, TC-FA-FAAC-80, TC-FA-FAAC-81 |

- Env var: `FA_AC_MA_RU_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Rujukan suite: seed dan pemulihan data lewat API/fixture BE, flag Guided Tooltip, dan sesi akun mengikuti `suite.md` (butir Hook suite). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: sembilan Asset Class contoh (Tabel Data Uji Pre-setup; nilai mengikuti Example Data PRD §4.1.1): HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Identitasnya dirujuk lewat `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada; nama kunci ditetapkan tim FE); langkah memakai nama seed literal sesuai TC. Spec ini mengubah VEHICLES (Class Name), OFFICE-OLD (status), BLDG, dan STORAGE (status).
- Tabel Asset Class memuat baris lain di luar sembilan Asset Class contoh (seed B-*, TEMP-EQ, dan sejenisnya); baris yang dipakai langkah dicari lewat Search kode Class Code karena tidak dijamin berada di halaman 1.
- Target aksi tulis memakai baris seed literal sesuai TC (nama seed dipakai apa adanya, pengecualian beralasan atas S-06 dan S-12 untuk modul ini); fixture BE (disediakan tim FE/BE) menyiapkan baris itu di hook `before` dan memulihkannya ke keadaan awal di hook `after`, termasuk bila spec gagal di tengah. Pemulihan juga dilakukan sebagai langkah penghubung antar blok (langkah 20); efek pada Last Updated dan entri audit trail dicatat dan tidak diasersi.
- Sesi API aktor (login API dengan password) dipakai sebagai pelaku pemulihan; kemampuan ini disediakan tim BE/FE dan dinyatakan di `suite.md`.
- Data Dinamis: tidak ada data bersuffix `{runId}`; target aksi tulis adalah baris seed literal di atas (pengecualian beralasan, lihat butir sebelumnya).
- State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).
- Kemampuan teknis: toggle kolom Active, dialog Konfirmasi, Bulk Action Bar, fixture BE untuk seed dan pemulihan, muat ulang halaman.

## Test Steps

### TC-FA-FAAC-78

1. Ketik Search `VEHICLES`, tekan Enter
2. Klik Class Code VEHICLES
3. Ubah Class Name menjadi Vehicles Updated
4. Klik [Save]
5. Verifikasi toast "Success, asset class has been updated." tampil di tabel Asset Class
6. Verifikasi tampilan kembali ke tabel Asset Class (tanpa versi Scheduled)
7. Verifikasi baris VEHICLES menampilkan Class Name "Vehicles Updated"

### TC-FA-FAAC-79

8. Ketik Search `OFFICE-OLD`, tekan Enter
9. Klik toggle kolom Active pada baris OFFICE-OLD (Off)
10. Verifikasi dialog Konfirmasi tampil dengan title "Activate Asset Class", bullet "OFFICE-OLD – Office Equipment (Legacy)", teks "Are you sure you want to activate it?", tombol [Cancel] dan [Activate]
11. Klik [Activate] pada dialog
12. Verifikasi toast "Success, asset class has been activated." tampil
13. Verifikasi toggle baris OFFICE-OLD berubah On

### TC-FA-FAAC-80

14. Ganti isi kotak search dengan `BLDG`, tekan Enter
15. Klik toggle kolom Active pada baris BLDG (On, 0 Asset Name)
16. Verifikasi dialog Konfirmasi tampil dengan title "Deactivate Asset Class", bullet "BLDG – Buildings", teks "Are you sure you want to deactivate it?", tombol [Cancel] dan [Deactivate]
17. Klik [Deactivate] pada dialog
18. Verifikasi toast "Success, asset class has been deactivated." tampil
19. Verifikasi toggle baris BLDG berubah Off
20. Pulihkan BLDG ke Active lewat fixture BE hingga status tersimpan, lalu muat ulang halaman (F5)

### TC-FA-FAAC-81

21. Ketik Search `BLDG`, tekan Enter
22. Centang baris BLDG (0 Asset Name)
23. Ganti isi kotak search dengan `STORAGE`, tekan Enter
24. Centang baris STORAGE (0 Asset Name); seleksi BLDG tetap terpilih
25. Klik Deactivate pada Bulk Action Bar
26. Verifikasi dialog Konfirmasi tampil dengan title "Deactivate Asset Classes", bullet "BLDG – Buildings" dan "STORAGE – Storage Equipment", teks "Are you sure you want to deactivate them?", tombol [Cancel] dan [Deactivate]
27. Klik [Deactivate] pada dialog
28. Verifikasi toast "Success, asset class has been deactivated." tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix positif (bagian 3a): aksi tulis Update (Save Edit, Activate, Deactivate, Bulk Deactivate) berhasil bagi role dengan huruf Update; satu role, tanpa ganti akun. Beberapa aksi dalam satu spec dengan polaritas seragam positif.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 20 (BLDG dipulihkan ke Active karena TC-FA-FAAC-80 menonaktifkannya dan TC-FA-FAAC-81 memerlukan BLDG Active; pelaku pemulihan memakai sesi API aktor, lihat `suite.md`).
- Post Condition TC-FA-FAAC-78 sampai 81 tidak punya langkah observasi di TC dan tidak diasersi.
- Temuan untuk QA:
  - TC-FA-FAAC-80 dan TC-FA-FAAC-81 sama-sama menonaktifkan BLDG; TC tidak menyebut pemulihan di antaranya sehingga spec menambah langkah 20.
  - TC-FA-FAAC-78 Expected b menyebut "(tanpa versi Scheduled)" dalam kurung tanpa menyebut surface pemeriksaannya; spec mengasersi tampilan kembali ke tabel tanpa asersi terpisah atas versi Scheduled.
