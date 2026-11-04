---
id: TC-FA-LIC-E2E-036-state-tenant-term-grace-expired-plan-starter-dan-toggle-off
title: "State Tenant: Term Grace atau Expired, Plan Starter, dan Toggle Alokasi per Grup OFF"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-450
  - TC-FA-LIC-549
  - TC-FA-LIC-614
coverage:
  web: automated
---

# State Tenant: Term Grace atau Expired, Plan Starter, dan Toggle Alokasi per Grup OFF

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Akun token TC-FA-LIC-614: Total Control client Paid dengan `License allocation per group` OFF (Pre-setup #35): `totalControlToggleOff_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TOGGLEOFF_TC_PASSWORD` (sesi API; tidak dipakai di UI).
- Data Pre-setup #12 (`Fixture.fixedAssetLicense.kuotaHierarki`): hierarki Produksi, Kantor Pusat (Divisi Logistik (Gudang A), Divisi IT, Divisi Keuangan), Cabang Surabaya, Cabang Medan dengan alokasi, Used, dan Reserved sesuai Example Data PRD §4.1.3; disediakan tim FE/BE. Divisi Logistik beralokasi 500; Divisi IT beralokasi 100; sesi Budi Santoso aktif (Pre-setup #14, disediakan tim FE/BE).
- Data Pre-setup #35 (`Fixture.fixedAssetLicense.toggleOff`): client Paid dengan `License allocation per group` OFF; Divisi Logistik beralokasi 500 dipertahankan.
- State global yang diubah spec: plan client Pre-setup #1 diturunkan ke Starter lewat fixture BE (TC-FA-LIC-549) lalu dipulihkan ke Paid, dan status term live diubah menjadi Grace (TC-FA-LIC-450); keduanya dipulihkan ke Pre-setup di hook `after` (tetap jalan walau spec gagal di tengah). Suite serial (`parallel: false`).
- S-06: target aksi tulis adalah alokasi grup Pre-setup #12 bernama literal yang hierarki dan kuotanya tidak dapat dimiliki spec. Pemulihan ke keadaan awal dijamin fixture BE (disediakan tim FE/BE, dinyatakan di `suite.md`) di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan Pre-setup #12"; efeknya (Last Updated grup, entri Changelog: Allocation Quota, System Log, dan Activity Log) tidak dipulihkan. Suite serial (`parallel: false`).
- Kemampuan teknis: klien HTTP yang mengirim request langsung ke server memakai token per akun (login API per akun pada tabel, tanpa browser; disediakan tim BE/FE) dan fixture BE untuk membaca state sesi, data alokasi, dan jumlah entri Changelog (disediakan tim FE/BE). Endpoint dan kontrak request mengikuti BE; TC tidak menuliskannya.
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.

## Test Steps

### TC-FA-LIC-614: Request langsung Edit dan Remove Allocation saat Paid dengan toggle OFF ditolak 403

1. Kirim request Edit Allocation `Divisi Logistik` = 600 memakai token Pre-setup #35
2. Verifikasi respons `403 Forbidden` seperti request tanpa capability
3. Kirim request Edit Allocation `Divisi Logistik` dengan nilai kosong (Remove Allocation) memakai token Pre-setup #35
4. Verifikasi respons `403 Forbidden` seperti request tanpa capability
5. Verifikasi Allocated Quota Divisi Logistik tetap 500 (baris alokasi dipertahankan) lewat fixture BE

### TC-FA-LIC-549: Request langsung Edit dan Remove Allocation saat plan Starter ditolak 403 dan baris alokasi tidak berubah

6. Turunkan plan client Total Control Pre-setup #1 menjadi Starter lewat fixture BE
7. Kirim request Edit Allocation `Divisi Logistik` = 600 memakai token Total Control Pre-setup #1
8. Verifikasi respons `403 Forbidden` untuk request Edit Allocation
9. Kirim request Edit Allocation `Divisi Logistik` dengan nilai kosong (Remove Allocation) memakai token yang sama
10. Verifikasi respons `403 Forbidden` untuk request Remove Allocation
11. Verifikasi Allocated Quota Divisi Logistik tetap 500 (baris alokasi dipertahankan) lewat fixture BE
12. Pulihkan plan client ke Paid dan Pre-setup #12 lewat fixture BE

### TC-FA-LIC-450: Term live Expired/Grace: aksi tulis License ditolak baku sedangkan tampilan baca tidak berubah

13. Catat data License Summary, Tab Allocation Quota, dan Tab Concurrent User sebagai baseline sebelum status term berubah
14. Ubah status term live menjadi `Grace` lewat fixture BE (sesi aktor sudah dibuka sebelum term Expired; sesi baru diblok, seat existing grandfathered)
15. Muat ulang halaman License
16. Verifikasi Tab `All License` tetap terbaca dengan data sama seperti baseline
17. Klik Tab `Allocation Quota`
18. Verifikasi Tab `Allocation Quota` tetap terbaca dengan data sama seperti baseline
19. Klik Tab `Concurrent User`
20. Verifikasi Tab `Concurrent User` tetap terbaca dengan data sama seperti baseline
21. Ketik Search `Budi Santoso`, tekan Enter
22. Klik `[Force Logout]` pada sesi Budi Santoso
23. Klik `[Confirm Logout]`
24. Verifikasi Force Logout ditolak `403 Forbidden`
25. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
26. Verifikasi dialog `Force Logout User` ditutup tanpa retry pada dialog yang sama
27. Verifikasi data Tab Concurrent User di-refresh
28. Klik `(←)` pada kotak Search
29. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
30. Klik `[Edit]` pada `Divisi IT`
31. Isi New Allocated Quota `120`
32. Klik `[Save]`
33. Verifikasi Edit Allocation ditolak `403 Forbidden`
34. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
35. Verifikasi modal Edit Allocation ditutup, input `120` dibuang, tanpa retry pada modal yang sama
36. Verifikasi data Tab Allocation Quota di-refresh

## Notes

- Spec kelas h (state tenant, bagian 3 prinsip 13) atas penolakan aksi tulis; TC-FA-LIC-549 dan 614 adalah request langsung kelas a yang hanya mengasersi respons dan state data dan berbagi state tenant (K-1: TC kelas a dengan Expected respons API tetap masuk spec FE+BE).
- Pembagian TC lintas spec: klausa "tidak ada entri log baru" pada Expected TC-FA-LIC-549 c dan TC-FA-LIC-614 c diasersi di spec absence 111 (request langsung ini sebagai pemicu, user dan baseline sendiri); spec ini hanya mengasersi status respons dan state data (S-05).
- Urutan blok: request langsung (TC-FA-LIC-614, 549) lebih dulu karena plan Starter menyembunyikan Tab Allocation Quota dan dipulihkan sebelum TC-FA-LIC-450 yang memakai UI.
- Langkah penghubung (aksi tanpa `Verifikasi`): "Catat data ... sebagai baseline", "Pulihkan plan client", "Muat ulang halaman License", Search `Budi Santoso` sebelum `[Force Logout]` dan `(←)` sesudahnya (tabel Active Sessions dapat memuat lebih dari satu halaman; 8b.13, R-16, S-09), dan "Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`".
- Spec di atas 35 langkah (36 langkah): ketiganya adalah satu kelas harness (state tenant) atas penolakan aksi tulis License dan setiap blok berdiri sendiri dengan state tenantnya sendiri.
- Temuan untuk QA:
  - TC-FA-LIC-450 "data sama seperti sebelum term Expired" tidak menyebut cara menangkap data sebelum perubahan; spec mencatat baseline sebelum status berubah.
  - TC-FA-LIC-614 memakai akun Pre-setup #35 hanya untuk token sesi API; langkah TC tidak membuka UI.
