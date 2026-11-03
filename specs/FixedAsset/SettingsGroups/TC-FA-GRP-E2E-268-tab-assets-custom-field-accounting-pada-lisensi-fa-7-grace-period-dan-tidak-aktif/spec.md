---
id: TC-FA-GRP-E2E-268-tab-assets-custom-field-accounting-pada-lisensi-fa-7-grace-period-dan-tidak-aktif
title: "Tab Assets Custom Field Accounting pada Lisensi FA-7: Grace Period Tersedia Read-Only dan Tidak Aktif Tidak Tersedia (Server Tidak Mengembalikan Nilai)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1261
  - TC-FA-GRP-1262
coverage:
  web: automated
---

# Tab Assets Custom Field Accounting pada Lisensi FA-7: Grace Period Tersedia Read-Only dan Tidak Aktif Tidak Tersedia (Server Tidak Mengembalikan Nilai)

## Prerequisites

- Mode: FE+BE.
- Hook suite: rujuk `suite.md` (login API aktor, sesi API, fixture BE, flag Guided Tooltip `fa-settings-groups` bernilai `seen`).
- Kelas harness h (state tenant/lisensi): kedua TC memakai client berstatus lisensi FA-7 khusus (Grace Period T-0 sampai T+30; tanpa FA-7 aktif maupun Grace). Client dan state lisensinya disediakan tim FE/BE lewat fixture BE (tidak ada endpoint di TC, PRD, atau LLD). Spec tidak mengubah lisensi; bila fixture BE mengubahnya untuk spec ini, pemulihan dijalankan di hook `after`.
- Akun aktor pertama: manageAccountingGrace (Pre-setup No 19: Global Role Manage accounting pada client Grace Period) `manageAccountingGrace_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_ACCGRACE_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): manageAccountingNoLic (Pre-setup No 20: Global Role Manage accounting pada client tanpa FA-7 aktif atau Grace) `manageAccountingNoLic_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_ACCNOLIC_PASSWORD`. Email dan password akun pada client khusus ini disediakan tim FE (lihat Temuan untuk QA).
- Data Pre-setup tambahan (hanya dibaca): Value Gate Node A (Tabel Dinamis No 10, aset G1-G6) pada masing-masing client, memakai nama literal Pre-setup yang dibaca bersama (tanpa seeding per spec dan tanpa cleanup; sama seperti 253 sampai 265); langkah dan asersi memakai nama itu. Cost Account: G1 `CA-100`, G3 belum diisi.
- Kemampuan teknis: membaca respons API data Tab Assets Value Gate Node A untuk aktor TC-1262 (klien HTTP dengan sesi API aktor, atau respons jaringan yang diamati browser; disediakan tim FE/BE tanpa endpoint karangan). Asersi hanya pada isi respons.
- Setup Column: hook `before` menghapus preferensi kolom Tab Assets di browser; hook `after` menghapus preferensi yang disimpan spec (kemampuan disediakan tim FE).

## Test Steps

### TC-1261: Kolom custom field Accounting pada lisensi FA-7 Grace Period tersedia dan read-only
1. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
2. Buka Detail Value Gate Node A (Tab Assets)
3. Buka Popup Setup Column
4. Verifikasi Cost Account tersedia di Popup Setup Column
5. Centang Cost Account, klik [Save]
6. Verifikasi sel Cost Account menampilkan nilai G1 `CA-100`
7. Verifikasi sel Cost Account G3 `—`
8. Verifikasi tabel read-only, tanpa aksi tulis pada tabel
### TC-1262: Kolom custom field Accounting pada lisensi FA-7 tidak aktif (selain Grace) tidak tersedia dan server tidak mengembalikan nilai
9. Ganti akun: Logout, login sebagai manageAccountingNoLic (`manageAccountingNoLic_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_GRP_ACCNOLIC_PASSWORD`), buka Fixed Asset > Settings > Groups
10. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
11. Buka Detail Value Gate Node A (Tab Assets)
12. Buka Popup Setup Column
13. Verifikasi Asset Value dan Warranty Expiry tersedia di Popup Setup Column
14. Verifikasi Cost Account tidak ada di Popup Setup Column
15. Baca respons API data Tab Assets Value Gate Node A
16. Verifikasi respons API memuat baris G1 (Asset Name atau nilai Asset Value)
17. Verifikasi respons API tidak memuat nilai Cost Account

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular. Kelas h dengan dua TC sejenis (lisensi FA-7 Grace dan tidak aktif).
- Langkah penghubung (S-03): satu langkah Ganti akun sebelum TC-1262 (client dan akun berbeda).
- Urutan assertion TC-1262: `Verifikasi` Asset Value dan Warranty Expiry tersedia ditaruh sebagai anchor positif sebelum absence Cost Account (8b butir 2); keduanya dari Expected a.
- Pembacaan respons API pada TC-1262 hanya mengasersi isi respons (8b butir 1), tidak ada asersi tampilan.
- Asersi tambahan (S-03, 8b butir 2): `Verifikasi` respons API memuat baris G1 sebagai anchor positif sebelum absence nilai Cost Account, supaya respons kosong atau gagal tidak meloloskan asersi.
- Langkah penghubung (S-03, S-14, R-16): sebelum tiap `Buka Detail` ditambahkan Search Groups List dengan nama group target (`Value Gate Node A`), karena client memiliki lebih dari 10 node level 1 dan page size 10 sehingga baris target tidak dijamin berada di halaman 1; Search hilang setelah F5, login, atau buka ulang halaman Groups sehingga dipasang lagi.
- Temuan untuk QA:
  - TC-1261 Expected b "tabel read-only, tanpa aksi tulis" tidak menyebut elemen yang diamati; spec mengasersi tidak ada aksi tulis pada tabel (selain kontrol Setup Column) sesuai kalimat TC.
  - Pre-setup No 19 dan No 20 tidak memuat nama client, email, dan password akun; precondition "T-0 sampai T+30" tidak menyebut cara menempatkan client pada jendela itu. Semua disediakan tim FE/BE.
  - Cara membaca "respons API data Tab Assets" tidak didefinisikan di TC, PRD, atau LLD (APISpec kosong).
