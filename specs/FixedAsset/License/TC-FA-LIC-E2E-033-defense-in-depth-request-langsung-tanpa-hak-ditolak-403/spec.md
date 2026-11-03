---
id: TC-FA-LIC-E2E-033-defense-in-depth-request-langsung-tanpa-hak-ditolak-403
title: "Defense-in-Depth: Request Langsung Tanpa Hak Ditolak 403"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-440
  - TC-FA-LIC-441
  - TC-FA-LIC-442
  - TC-FA-LIC-443
  - TC-FA-LIC-444
  - TC-FA-LIC-531
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung Tanpa Hak Ditolak 403

## Prerequisites

- Mode: FE+BE.
- Akun: login UI Total Control Pre-setup #1 di hook `before` hanya sebagai sesi default (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`); token akun lain diperoleh lewat login API.
- Akun yang diuji (token per akun; Tabel Data Uji Pre-setup #2, #4, #5, #6, #8, #29):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-FA-LIC-440, TC-FA-LIC-441 | Read Only (Pre-setup #2) | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
| TC-FA-LIC-440, TC-FA-LIC-442 | Manage asset license (Kantor Pusat) (Pre-setup #4) | `manageAssetLicenseHQ_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAL_HQ_PASSWORD` |
| TC-FA-LIC-440, TC-FA-LIC-443 | Group Manager (Kantor Pusat) (Pre-setup #6) | `groupManagerHQ_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_HQ_PASSWORD` |
| TC-FA-LIC-440, TC-FA-LIC-441 | Role lain tanpa capability License (Pre-setup #8) | `noCapability_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_NOCAP_PASSWORD` |
| TC-FA-LIC-444 | Manage asset license tumpang tindih (Kantor Pusat dan Divisi Logistik) (Pre-setup #5) | `manageAssetLicenseOverlap_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAL_OVERLAP_PASSWORD` |
| TC-FA-LIC-531 | Group Manager tumpang tindih (Kantor Pusat dan Divisi Logistik) (Pre-setup #29) | `groupManagerOverlap_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_OVERLAP_PASSWORD` |

  Seluruh nama env pada tabel adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Request TC-FA-LIC-442 (token Pre-setup #4, di-assign pada Kantor Pusat), satu baris tabel per request:

| No | Request | Target |
|---|---|---|
| 1 | Edit Allocation | `Kantor Pusat` = 1600 |
| 2 | Remove Allocation (nilai kosong) | `Kantor Pusat` |
| 3 | Edit Allocation | `Produksi` = 1600 |
| 4 | Edit Allocation | `Cabang Medan` (level 1) = 1100 |

- Request TC-FA-LIC-443 (token Pre-setup #6, ditugaskan pada Kantor Pusat), satu baris tabel per request:

| No | Request | Target |
|---|---|---|
| 1 | Edit Allocation | `Kantor Pusat` = 1600 |
| 2 | Edit Allocation | `Produksi` = 1600 |

- Data Pre-setup #12 (`Fixture.fixedAssetLicense.kuotaHierarki`): hierarki Produksi, Kantor Pusat (Divisi Logistik (Gudang A), Divisi IT, Divisi Keuangan), Cabang Surabaya, Cabang Medan dengan alokasi, Used, dan Reserved sesuai Example Data PRD §4.1.3; disediakan tim FE/BE. Divisi Logistik beralokasi 500.
- Data Pre-setup #14 (`Fixture.fixedAssetLicense.sesiAktif`): 18 sesi aktif PT Sejahtera, seat 25, termasuk sesi Budi Santoso (akun login Budi Santoso disediakan tim FE); disediakan tim FE/BE.
- S-06: TC-FA-LIC-444 dan 531 mengubah alokasi Divisi Logistik Pre-setup #12 (bernama literal, kuotanya tidak dapat dimiliki spec); pemulihan dijamin fixture BE (dinyatakan di `suite.md`) di hook `before` dan `after` serta sebagai langkah "Pulihkan Pre-setup #12"; efeknya (entri Changelog, System Log, Activity Log) tidak dipulihkan. Suite serial (`parallel: false`).
- Kemampuan teknis: klien HTTP yang mengirim request langsung ke server memakai token per akun (login API per akun pada tabel, tanpa browser; disediakan tim BE/FE) dan fixture BE untuk membaca state sesi, data alokasi, dan jumlah entri Changelog (disediakan tim FE/BE). Endpoint dan kontrak request mengikuti BE; TC tidak menuliskannya.
- Sesi UI Total Control Pre-setup #1 dibuka hook `before` dan halaman License dibuka hook `beforeEach`; langkah request langsung tidak melewati browser.
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.

## Test Steps

### TC-FA-LIC-440: Request langsung Force Logout tanpa hak ditolak 403 (Read Only, Manage asset license, Group Manager, role lain)

1. Untuk setiap akun pada tabel (token Pre-setup #2, #4, #6, #8; langkah 1 sampai 2 diulang per token): kirim request langsung ke endpoint Force Logout untuk sesi Budi Santoso memakai token akun itu
2. Verifikasi respons `403 Forbidden` untuk token akun itu
3. Verifikasi sesi Budi Santoso tetap aktif lewat fixture BE

### TC-FA-LIC-441: Request langsung Edit/Remove Allocation tanpa hak ditolak 403 (Read Only dan role lain)

4. Untuk setiap akun pada tabel (token Pre-setup #2 dan #8; langkah 4 sampai 7 diulang per token): kirim request Edit Allocation `Divisi Logistik` = 600 memakai token akun itu
5. Verifikasi respons `403 Forbidden` untuk request Edit Allocation
6. Kirim request Remove Allocation (nilai kosong) pada `Divisi Logistik` memakai token yang sama
7. Verifikasi respons `403 Forbidden` untuk request Remove Allocation
8. Verifikasi Allocated Quota Divisi Logistik tetap 500 lewat fixture BE

### TC-FA-LIC-442: Manage asset license: Edit/Remove pada grup yang di-assign (non-descendant) atau di luar scope via API ditolak 403

9. Untuk setiap baris tabel request TC-FA-LIC-442 (langkah 9 sampai 10 diulang per baris): kirim request baris itu memakai token Pre-setup #4
10. Verifikasi respons `403 Forbidden`
11. Verifikasi alokasi `Kantor Pusat`, `Produksi`, dan `Cabang Medan` tidak berubah lewat fixture BE

### TC-FA-LIC-443: Group Manager: Edit via API pada grup yang ditugaskan (non-descendant) ditolak 403

12. Untuk setiap baris tabel request TC-FA-LIC-443 (langkah 12 sampai 13 diulang per baris): kirim request baris itu memakai token Pre-setup #6
13. Verifikasi respons `403 Forbidden`
14. Verifikasi alokasi `Kantor Pusat` dan `Produksi` tidak berubah lewat fixture BE

### TC-FA-LIC-444: Manage asset license dengan assignment tumpang tindih: Edit descendant via API berhasil (union)

15. Kirim request Edit Allocation `Divisi Logistik` = 600 memakai token Pre-setup #5
16. Verifikasi respons `200 OK` untuk Edit Divisi Logistik
17. Kirim request Edit Allocation `Kantor Pusat` = 1600 memakai token Pre-setup #5
18. Verifikasi respons `403 Forbidden` untuk Edit Kantor Pusat
19. Verifikasi Allocated Quota Divisi Logistik = 600 lewat fixture BE
20. Pulihkan Pre-setup #12 lewat fixture BE

### TC-FA-LIC-531: Group Manager dengan assignment tumpang tindih: Edit descendant via API berhasil (union), grup level 1 ditolak

21. Kirim request Edit Allocation `Divisi Logistik` = 650 memakai token Pre-setup #29
22. Verifikasi respons `200 OK` untuk Edit Divisi Logistik
23. Kirim request Edit Allocation `Kantor Pusat` = 1600 memakai token Pre-setup #29
24. Verifikasi respons `403 Forbidden` untuk Edit Kantor Pusat
25. Verifikasi Allocated Quota Divisi Logistik = 650 lewat fixture BE
26. Pulihkan Pre-setup #12 lewat fixture BE

## Notes

- K-1: TC kelas a (defense-in-depth) dengan Expected respons API tetap masuk spec FE+BE walau tumpang tindih dengan TC backend, karena tiap TC granular tepat satu spec. Spec hanya mengasersi status respons dan state data (bagian 8b butir 1), bukan perilaku FE.
- Pembagian TC lintas spec: klausa "tidak ada entri log" pada Expected TC-FA-LIC-440 b dan TC-FA-LIC-441 b diasersi di spec absence 111 (request langsung ini sebagai pemicu, user dan baseline sendiri); spec ini hanya mengasersi status respons dan state data (S-05).
- Langkah "Untuk setiap akun pada tabel" dan "Untuk setiap baris tabel request" adalah idiom perulangan (bagian 8b butir 7): langkah 1 sampai 2, 4 sampai 7, 9 sampai 10, dan 12 sampai 13 diulang per token atau per baris; `Verifikasi` tiap iterasi tetap satu per klausa.
- Langkah penghubung (aksi tanpa `Verifikasi`): "Pulihkan Pre-setup #12".
- Temuan untuk QA:
  - TC-FA-LIC-440 sampai 444 dan 531 tidak menyebut endpoint; kontrak request disediakan tim BE.
  - TC-FA-LIC-442 langkah 5 memeriksa data alokasi tiga grup; spec memeriksanya satu kali setelah keempat request.
