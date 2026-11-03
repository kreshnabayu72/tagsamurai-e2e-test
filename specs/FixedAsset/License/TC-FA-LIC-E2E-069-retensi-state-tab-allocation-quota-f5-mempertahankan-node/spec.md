---
id: TC-FA-LIC-E2E-069-retensi-state-tab-allocation-quota-f5-mempertahankan-node
title: "Retensi State Tab Allocation Quota: Muat Ulang (F5) Mempertahankan Node dan Pindah Tab Mereset Node"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-220
  - TC-FA-LIC-537
coverage:
  web: automated
---
# Retensi State Tab Allocation Quota: Muat Ulang (F5) Mempertahankan Node dan Pindah Tab Mereset Node

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #12 (hanya dibaca): hierarki PT Sejahtera dengan grup level 1 Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat (Divisi Logistik, Divisi IT, Divisi Keuangan); Data Pre-setup #13 (riwayat) dan #14 (sesi aktif) untuk Tab lain; lewat `Fixture.fixedAssetLicense.kuotaHierarki`, `.riwayat`, dan `.sesiAktif` (fixture belum ada; disediakan tim FE/BE).
- State yang diubah dan dipulihkan: node terpilih Sidebar dan Search Section 2 (direset oleh perpindahan Tab pada langkah 16 dan 24).

## Test Steps

### TC-FA-LIC-220: Muat ulang (F5) di Tab Allocation Quota

1. Klik sub-tab `Allocation History`
2. Klik Tab `Allocation Quota`
3. Verifikasi node aktif `All Groups` di Sidebar Group Tree pada pembukaan pertama Tab
4. Klik node `Kantor Pusat` di Sidebar
5. Ketik Search `Logistik` pada Search tabel Section 2, tekan Enter
6. Tekan F5
7. Verifikasi halaman tetap di Tab `Allocation Quota` dengan breadcrumb `License > Allocation Quota`
8. Verifikasi node `Kantor Pusat` tetap terpilih
9. Verifikasi Search `Logistik` tetap terisi
10. Verifikasi Section 2 hanya memuat `Divisi Logistik`
11. Verifikasi Sort dan paginasi tetap seperti sebelum F5 (Sort default, halaman 1)
12. Klik Tab `All License`
13. Verifikasi sub-tab aktif kembali ke `Subscription History`
14. Klik Tab `Allocation Quota`
15. Verifikasi node aktif kembali ke `All Groups`
16. Verifikasi state tabel Section 2 direset (Search kosong, Sort default, halaman 1)

### TC-FA-LIC-537: Pindah Tab License lain lalu kembali ke Allocation Quota

17. Klik node `Kantor Pusat` di Sidebar
18. Ketik Search `Divisi` pada Search Child Groups Quota, tekan Enter
19. Klik Tab `Concurrent User`
20. Klik Tab `Allocation Quota`
21. Verifikasi node `All Groups` terpilih di Sidebar dan Context Header `All Groups` (bukan `Kantor Pusat (GRP-HQ)`)
22. Verifikasi Section 1 berjudul `All License`
23. Verifikasi Section 2 berjudul `Level 1 Groups Quota`
24. Verifikasi Search `Divisi` tidak lagi aktif pada tabel Group License Allocation

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Urutan TC dalam spec: 220, 537. TC-FA-LIC-220 memiliki Dependensi TC-FA-LIC-218; langkah TC-FA-LIC-218 yang dibutuhkan (Search di sub-tab riwayat) tidak diasersi di TC-FA-LIC-220 sehingga cukup langkah membuka sub-tab `Allocation History` (S-04).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): klik Tab dan sub-tab sebagai aksi deterministik, serta langkah pertama (membuka sub-tab `Allocation History` sebagai syarat langkah TC-FA-LIC-220).
- Asersi di luar Expected TC (S-03): `Verifikasi` Sort dan paginasi tetap (langkah pada TC-FA-LIC-220) memenuhi klausa "Search, Filter, Sort, dan paginasi yang aktif sebelum F5 tetap sama"; state yang aktif sebelum F5 hanya Search sehingga Sort dan paginasi diasersi pada nilai default.
- Temuan untuk QA:
  - TC-FA-LIC-220 menulis klausa "Search, Filter, Sort, dan paginasi yang aktif sebelum F5 tetap sama" sedangkan langkah TC hanya mengaktifkan Search; Filter, Sort, dan paginasi tidak aktif di luar nilai default.
  - TC-FA-LIC-220 dan 537 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
