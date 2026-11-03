---
id: TC-FA-CAID-E2E-098-pencatatan-log-absence-request-otorisasi-ditolak
title: "Pencatatan Log Absence: Request Save dan Toggle Langsung Ditolak Tanpa Entri Log"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAID-303
  - TC-FA-CAID-304
  - TC-FA-CAID-305
coverage:
  web: automated
---

# Pencatatan Log Absence: Request Save dan Toggle Langsung Ditolak Tanpa Entri Log

## Prerequisites

- Mode: FE+BE.
- Akun pengamat: Total Control Company Alpha (Pre-setup No 1, `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`) untuk TC-FA-CAID-303 dan TC-FA-CAID-304; login di hook `before` spec ini, halaman dibuka hook `beforeEach` suite. Request dikirim lewat klien HTTP dengan token sesi API role pada tabel (token tidak dihitung sebagai sesi web, sehingga sesi UI tidak diusir).
- Role yang diuji untuk TC-FA-CAID-303 dan TC-FA-CAID-304 (Company Alpha; email `<prefix>_automated_{namaCompany}@qwertysystem.net`, password dari env, tidak ditulis di spec atau fixture). Langkah tiap role identik, hanya token sesi API yang berbeda:

| Role | Pre-setup | Prefix email | Env password |
|---|---|---|---|
| Read Only | No 2 | `readOnly` | `Spectra.env.FA_RO_PASSWORD` |
| Config-Read (Manage asset ID configuration hanya Read) | No 4 | `configRead` | `Spectra.env.FA_CFGREAD_PASSWORD` |
| Master-Data-Only (Manage asset master data tanpa Manage asset ID configuration) | No 5 | `masterDataOnly` | `Spectra.env.FA_MDONLY_PASSWORD` |
| Tanpa Role Terkait | No 7 | `noRelatedRole` | `Spectra.env.FA_NOROLE_PASSWORD` |

- Akun TC-FA-CAID-305: Config-Update (Manage asset ID configuration dengan Read dan Update, Pre-setup No 3) pada Company Starter (Pre-setup No 13). Email akun pada Company Starter tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE. Password dari `Spectra.env.FA_STARTER_CFGUPD_PASSWORD` (nama usulan, perlu konfirmasi tim FE). Ganti akun ditulis sebagai langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 dan aset A1 sampai A5 (Pre-setup No 11) di `beforeEach` dan `after` lewat sesi API aktor. Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company). Data Pre-setup No 13: Company Starter dengan konfigurasi tersimpan B1 dan aset S1 `JKT/LAP/T490/0926/1`. Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): klien API dan penyunting request pada sesi otomasi (Pre-setup No 26) untuk mengirim request Save dan Toggle langsung ke server; kemampuan membaca jumlah entri Object `Custom Asset ID` di Modal Changelog: Custom Asset ID, System Log (Detail User), dan Activity Log (tab User Action) sebelum dan sesudah request (audit trail permanen sehingga jumlah entri diasersi sebagai selisih terhadap baseline, S-12).
- State: tidak ada perubahan tersimpan yang diharapkan; semua request ditolak. Entri log yang sudah ada tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-303: Request Save langsung tanpa capability Update tidak menulis entri log

1. Catat baseline jumlah entri Object `Custom Asset ID` pada Modal Changelog: Custom Asset ID, System Log (Detail pengguna Sarah Johnson), dan Activity Log (tab User Action)

Untuk setiap baris tabel Role yang diuji (langkah 2 sampai 3):

2. Kirim request Save konfigurasi langsung ke server dengan token sesi API role pada baris tabel, Separator `- (Dash)`, formula valid delapan segmen
3. Verifikasi server mengembalikan HTTP 403 Forbidden

Setelah keempat role:

4. Buka Modal Changelog: Custom Asset ID
5. Verifikasi tabel Changelog termuat dengan header kolom tampil
6. Verifikasi jumlah entri Changelog tidak bertambah dibanding baseline
7. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
8. Verifikasi tabel System Log termuat dengan header kolom tampil
9. Verifikasi jumlah entri System Log tidak bertambah dibanding baseline
10. Buka Fixed Asset > Activity Log > tab User Action
11. Verifikasi tabel Activity Log termuat dengan header kolom tampil
12. Verifikasi jumlah entri Activity Log tidak bertambah dibanding baseline

### TC-FA-CAID-304: Request Toggle langsung tanpa capability Update tidak menulis entri log

13. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada Modal Changelog, System Log, dan Activity Log

Untuk setiap baris tabel Role yang diuji (langkah 14 sampai 15):

14. Kirim request Toggle langsung ke server dengan token sesi API role pada baris tabel, status Master Switch `Inactive`
15. Verifikasi server mengembalikan HTTP 403 Forbidden

Setelah keempat role:

16. Buka Modal Changelog: Custom Asset ID
17. Verifikasi tabel Changelog termuat dengan header kolom tampil
18. Verifikasi jumlah entri Changelog tidak bertambah dibanding baseline
19. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
20. Verifikasi tabel System Log termuat dengan header kolom tampil
21. Verifikasi jumlah entri System Log tidak bertambah dibanding baseline
22. Buka Fixed Asset > Activity Log > tab User Action
23. Verifikasi tabel Activity Log termuat dengan header kolom tampil
24. Verifikasi jumlah entri Activity Log tidak bertambah dibanding baseline

### TC-FA-CAID-305: Request Save dan Toggle langsung pada plan Starter tidak menulis entri Changelog

25. Ganti akun: logout akun Total Control, lalu login sebagai Config-Update pada Company Starter (Pre-setup No 13)
26. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada Modal Changelog: Custom Asset ID
27. Kirim request Save langsung ke server dengan Separator `- (Dash)`
28. Verifikasi request Save ditolak server
29. Kirim request Toggle langsung ke server dengan status `Inactive`
30. Verifikasi request Toggle ditolak server
31. Buka Modal Changelog: Custom Asset ID
32. Verifikasi tabel Changelog termuat dengan header kolom tampil
33. Verifikasi jumlah entri Changelog tidak bertambah dibanding baseline

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 33 langkah nominal, 45 langkah dengan ekspansi dua perulangan empat role (langkah 2 sampai 3 dan 14 sampai 15), di atas smell 35 langkah. Alasan: seluruhnya satu kelas harness (kelas g, asersi absence log atas request langsung yang ditolak) dan tiap TC punya baseline sendiri; blok baca-log berpola (buka surface, `Verifikasi` tabel termuat, `Verifikasi` jumlah) tidak dihitung menurut bagian 3 prinsip 13 (langkah 4 sampai 12, 16 sampai 24, dan 31 sampai 33), sehingga langkah di luar blok itu 12 (24 dengan ekspansi).
- Bagian 8b butir 1 dan `P-5` butir (a): request langsung ke server adalah pemicu yang hanya membentuk kondisi yang diasersi tidak tercatat; asersinya hanya status respons (anchor penolakan) dan jumlah entri log terhadap baseline. Perilaku FE atas respons yang sama tidak diasersi.
- Anchor positif asersi absence (bagian 8b butir 2): jumlah awal yang dicatat pada langkah 1, 13, dan 26, status penolakan server pada langkah 3, 15, 28, dan 30, serta `Verifikasi` tabel log termuat dengan header kolom pada tiap surface sebelum jumlah diasersi.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 13, dan 26 (mencatat baseline, S-12), langkah 4, 7, 10, 16, 19, 22, dan 31 (membuka surface log), langkah 25 (ganti akun).
- Pembagian TC lintas spec: TC-FA-CAID-303, 304, dan 305 juga ada di spec 026 yang hanya mengasersi status respons dan state data (konfigurasi tersimpan dan Asset ID); TC-FA-CAID-306 sampai 309, 337, dan 338 ada di spec 099; TC-FA-CAID-312 dan 313 ada di spec 100.
- Temuan untuk QA:
  - TC-FA-CAID-303 b dan TC-FA-CAID-304 b menyebut "System Log pada Detail User aktor"; aktor di sini adalah anggota role pengirim request, sedangkan Langkah Uji membaca layar sebagai Total Control. Spec membaca System Log pada Detail pengguna Sarah Johnson sebagai Total Control, sama seperti spec 042; bila yang dimaksud System Log tiap anggota role, perlu penegasan di TC.
  - Email akun Config-Update pada Company Starter tidak tertulis di Pre-setup TC; nama env var password adalah usulan.
  - TC-FA-CAID-305 c hanya menyebut Modal Changelog; spec tidak mengasersi System Log dan Activity Log untuk TC itu.
  - TC-FA-CAID-305 a menyebut alasan penolakan ("plan tidak memiliki toggle Asset ID Config dan tidak ada mass update yang berjalan") tanpa langkah observasi; alasan itu tidak diasersi.
  - Post Condition TC-FA-CAID-303, 304, dan 305 tidak diasersi karena TC tidak memberi langkah observasinya.
