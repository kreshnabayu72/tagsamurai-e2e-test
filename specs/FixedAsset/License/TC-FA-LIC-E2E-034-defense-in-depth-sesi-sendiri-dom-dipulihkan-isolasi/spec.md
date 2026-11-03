---
id: TC-FA-LIC-E2E-034-defense-in-depth-sesi-sendiri-dom-dipulihkan-isolasi
title: "Defense-in-Depth: Sesi Sendiri, DOM Dipulihkan, Isolasi Tenant, dan Payload Tidak Valid"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-445
  - TC-FA-LIC-446
  - TC-FA-LIC-451
  - TC-FA-LIC-453
  - TC-FA-LIC-544
coverage:
  web: automated
---

# Defense-in-Depth: Sesi Sendiri, DOM Dipulihkan, Isolasi Tenant, dan Payload Tidak Valid

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun lain pada tabel "Role yang diuji" lewat langkah Ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; seluruh nama env pada tabel adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Akun yang diuji: Total Control Pre-setup #1 untuk seluruh blok kecuali TC-FA-LIC-446 (Read Only):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-FA-LIC-445, TC-FA-LIC-451, TC-FA-LIC-453, TC-FA-LIC-544 | Total Control (Pre-setup #1) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| TC-FA-LIC-446 | Read Only (Pre-setup #2) | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |

- Data Pre-setup #12 (`Fixture.fixedAssetLicense.kuotaHierarki`): hierarki Produksi, Kantor Pusat (Divisi Logistik (Gudang A), Divisi IT, Divisi Keuangan), Cabang Surabaya, Cabang Medan dengan alokasi, Used, dan Reserved sesuai Example Data PRD §4.1.3; disediakan tim FE/BE. Divisi IT beralokasi 100; Divisi Logistik beralokasi 500.
- Data Pre-setup #14 (`Fixture.fixedAssetLicense.sesiAktif`): 18 sesi aktif PT Sejahtera, seat 25, termasuk sesi Budi Santoso (akun login Budi Santoso disediakan tim FE); disediakan tim FE/BE. Akun Pre-setup #1 memiliki dua sesi aktif (dua perangkat) untuk TC-FA-LIC-445; sesi kedua dibuat lewat sesi API di hook `before`.
- Data TC-FA-LIC-451: client B (client lain beserta group id milik client B) tidak tertulis di Pre-setup TC; disediakan tim FE/BE.
- Data TC-FA-LIC-544: Gudang A tanpa alokasi dengan Used 100 (Minimum Quota 100) diatur lewat fixture BE; parent Divisi Logistik beralokasi 500 tanpa child beralokasi.
- Kemampuan teknis: memunculkan tombol tersembunyi lewat manipulasi DOM di browser (TC-FA-LIC-446; disediakan tim FE).
- S-06: target aksi tulis adalah alokasi grup Pre-setup #12 bernama literal yang hierarki dan kuotanya tidak dapat dimiliki spec. Pemulihan ke keadaan awal dijamin fixture BE (disediakan tim FE/BE, dinyatakan di `suite.md`) di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan Pre-setup #12"; efeknya (Last Updated grup, entri Changelog: Allocation Quota, System Log, dan Activity Log) tidak dipulihkan. Suite serial (`parallel: false`).
- Kemampuan teknis: klien HTTP yang mengirim request langsung ke server memakai token per akun (login API per akun pada tabel, tanpa browser; disediakan tim BE/FE) dan fixture BE untuk membaca state sesi, data alokasi, dan jumlah entri Changelog (disediakan tim FE/BE). Endpoint dan kontrak request mengikuti BE; TC tidak menuliskannya.
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.

## Test Steps

### TC-FA-LIC-445: Force Logout atas sesi sendiri via API ditolak server tanpa dialog khusus dan tanpa log

1. Kirim request Force Logout untuk sesi milik aktor sendiri (Pre-setup #1) memakai token Pre-setup #1
2. Verifikasi respons akses ditolak (`403 Forbidden`)
3. Verifikasi kedua sesi aktor tetap aktif lewat fixture BE

### TC-FA-LIC-451: Isolasi tenant: request Edit atas group id milik client lain ditolak

4. Kirim request Edit Allocation dengan group id milik client B memakai token Total Control client A
5. Verifikasi respons `403 Forbidden`
6. Verifikasi respons tidak membocorkan data client B
7. Verifikasi data alokasi grup client B tidak berubah lewat fixture BE

### TC-FA-LIC-453: Payload Allocated Quota non-bilangan-bulat via API ditolak server tanpa mengubah data

8. Untuk setiap nilai pada tabel (`12.5`, `-5`, `abc`, `1e3`; langkah 8 sampai 9 diulang per nilai): kirim request Edit Allocation dengan nilai itu memakai token Pre-setup #1
9. Verifikasi request ditolak server
10. Verifikasi Allocated Quota tidak berubah lewat fixture BE

### TC-FA-LIC-544: Request langsung Edit Allocation di bawah Minimum Quota saat parent tidak lagi beralokasi ditolak karena precondition parent

11. Atur Gudang A tanpa alokasi dengan Used 100 (Minimum Quota 100) lewat fixture BE; parent Divisi Logistik beralokasi 500 tanpa child beralokasi
12. Kirim request Edit Allocation `Divisi Logistik` dengan nilai kosong (Remove Allocation) memakai token Pre-setup #1, sehingga parent Gudang A tidak lagi beralokasi
13. Catat data alokasi `Divisi Logistik` dan `Gudang A` serta jumlah entri Changelog: Allocation Quota lewat fixture BE
14. Kirim request Edit Allocation `Gudang A` = 50 (di bawah Minimum Quota 100) memakai token yang sama
15. Verifikasi request ditolak server tanpa mengubah data karena parent `Divisi Logistik` tidak lagi beralokasi (penolakan precondition parent)
16. Verifikasi penolakan yang berlaku adalah penolakan precondition parent, bukan penolakan Minimum Quota (V-FALIC-01), walau 50 di bawah Minimum Quota 100
17. Verifikasi `Divisi Logistik` dan `Gudang A` tetap tanpa alokasi
18. Verifikasi jumlah entri Changelog: Allocation Quota sama dengan yang dicatat
19. Pulihkan Pre-setup #12 lewat fixture BE

### TC-FA-LIC-446: Elemen Hidden dipulihkan lewat DOM tetap ditolak server

20. Ganti akun: logout, lalu login sebagai Read Only dengan `Spectra.env.FA_RO_PASSWORD`
21. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
22. Munculkan tombol `[Edit]` tersembunyi pada Divisi IT lewat manipulasi DOM
23. Klik tombol `[Edit]` yang dimunculkan
24. Isi New Allocated Quota `120`
25. Klik `[Save]`
26. Verifikasi server menolak dengan `403 Forbidden`
27. Verifikasi toast baku `You don't have permission to do this.` tampil
28. Verifikasi UI di-refresh dan tombol `[Edit]` kembali tersembunyi
29. Verifikasi data tidak berubah: Allocated Quota Divisi IT tetap 100

## Notes

- K-1: TC kelas a (defense-in-depth) dengan Expected respons API tetap masuk spec FE+BE walau tumpang tindih dengan TC backend, karena tiap TC granular tepat satu spec. Spec hanya mengasersi status respons dan state data (bagian 8b butir 1), bukan perilaku FE.
- Pembagian TC lintas spec: klausa "tidak ada entri System Log atau Activity Log" pada Expected TC-FA-LIC-445 b dan "tidak ada entri log" pada TC-FA-LIC-453 a diasersi di spec absence 111 (request langsung ini sebagai pemicu, user dan baseline sendiri); spec ini hanya mengasersi status respons dan state data (S-05).
- Urutan blok: blok request langsung (TC-FA-LIC-445, 451, 453, 544) lebih dulu dan TC-FA-LIC-446 terakhir karena memakai akun Read Only. TC-FA-LIC-452 dan 454 ada di spec `TC-FA-LIC-E2E-167`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 19 "Pulihkan Pre-setup #12" dan "Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`" setelah ganti akun (langkah 21).
- Temuan untuk QA:
  - TC-FA-LIC-451 memakai client B yang tidak tertulis di Pre-setup TC.
  - TC-FA-LIC-544 Expected b tidak menyebut tanda teramati yang membedakan penolakan precondition parent dari penolakan Minimum Quota (kode atau pesan galat); disediakan tim BE.
