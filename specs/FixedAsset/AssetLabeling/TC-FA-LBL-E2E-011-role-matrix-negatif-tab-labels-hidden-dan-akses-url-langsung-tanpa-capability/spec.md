---
id: TC-FA-LBL-E2E-011-role-matrix-negatif-tab-labels-hidden-dan-akses-url-langsung-tanpa-capability
title: "Role Matrix Negatif: Tab Labels Hidden dan Akses URL Langsung tanpa Capability"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-32
  - TC-FA-LBL-33
  - TC-FA-LBL-511
coverage:
  web: automated
---

# Role Matrix Negatif: Tab Labels Hidden dan Akses URL Langsung tanpa Capability

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya. Karena tab Labels tidak tersedia untuk kedua akun spec ini, layar awal yang dibuka adalah Fixed Asset > Settings > Asset Master.
- Role yang diuji (Tanpa Role Ini login di hook `before` spec ini menggantikan akun default suite; Group Manager lewat langkah Ganti akun; hook `after` mengembalikan sesi ke akun default suite, Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`):

| Role | Pre-setup | Akun (Fixture) | Env | TC | Langkah |
|---|---|---|---|---|---|
| Tanpa Role Ini (tanpa capability Manage Asset Master Data) | #8 | `Fixture.assetLabeling.akun.noRole` | `Spectra.env.FA_NOROLE_PASSWORD` | TC-FA-LBL-32, TC-FA-LBL-33 | 1 sampai 9 |
| Group Manager tanpa capability | #34 | `Fixture.assetLabeling.akun.groupManagerNoCap` | `Spectra.env.FA_GMNOCAP_PASSWORD` | TC-FA-LBL-511 | 10 sampai 12 |

- Environment variable: `FA_NOROLE_PASSWORD`, `FA_GMNOCAP_PASSWORD`, `FA_LBL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun dan URL tanpa rahasia; fixture ini belum ada dan disediakan tim FE. `Fixture.assetLabeling.urlTabLabels` adalah URL tab Labels Asset Master yang dibuka langsung di address bar (TC tidak menulis URL-nya).
- State global: tidak ada yang diubah selain sesi login. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### Tanpa Role Ini: TC-FA-LBL-32

1. Verifikasi Tab `Asset Name` dan `Custom Asset ID` tampil di daftar tab Asset Master
2. Verifikasi Tab `Labels` tidak dirender di daftar tab
3. Verifikasi tidak ada tab berlabel `Labels` yang dapat diklik

### Tanpa Role Ini: TC-FA-LBL-33

4. Klik beranda Fixed Asset
5. Buka URL `Fixture.assetLabeling.urlTabLabels` langsung di address bar
6. Verifikasi toast error `You don't have permission to do this.`
7. Verifikasi tidak ada redirect ke halaman unauthorized terpisah
8. Verifikasi UI di-refresh sehingga elemen yang tidak berhak tidak tampil
9. Verifikasi daftar label tidak dimuat

### Group Manager tanpa capability: TC-FA-LBL-511

10. Ganti akun: Logout, login sebagai Group Manager tanpa capability `Fixture.assetLabeling.akun.groupManagerNoCap` (`Spectra.env.FA_GMNOCAP_PASSWORD`), buka Fixed Asset > Settings > Asset Master
11. Verifikasi Tab `Asset Name` dan `Custom Asset ID` tampil di daftar tab Asset Master
12. Verifikasi Tab `Labels` tidak dirender

## Notes

- Spec ditulis per blok role dengan langkah Ganti akun eksplisit (langkah 10) karena akun pertama login di hook `before` (bagian 3a, varian A).
- Langkah penghubung (S-03): langkah 4 (kembali ke beranda Fixed Asset sebagai keadaan awal TC-FA-LBL-33) dan langkah 1 serta 11 (Verifikasi tab lain tampil sebagai anchor positif untuk asersi `Hidden` langkah 2 dan 12, bagian 8b butir 2).
- Absence pada langkah 7 dan 9: toast error langkah 6 dan UI yang di-refresh (langkah 8) menjadi anchor positif bahwa halaman termuat.
- Langkah 12 mencakup butir "tier Group Manager saja tidak memberi akses ke katalog Label" (kesimpulan dari tab `Labels` tidak dirender yang tidak teramati terpisah, S-03).
- Temuan untuk QA: TC-FA-LBL-33 tidak menulis URL tab Labels dan tidak menyebut "UI di-refresh" secara teramati; spec memakai `Fixture.assetLabeling.urlTabLabels` (disediakan tim FE) dan mengasersi elemen tab `Labels` tidak tampil.
