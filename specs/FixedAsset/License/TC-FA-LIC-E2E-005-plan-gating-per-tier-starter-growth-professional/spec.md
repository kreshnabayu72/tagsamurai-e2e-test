---
id: TC-FA-LIC-E2E-005-plan-gating-per-tier-starter-growth-professional
title: "Role Matrix: Plan Gating per Tier Starter, Growth, Professional, dan Enterprise"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-435
  - TC-FA-LIC-436
  - TC-FA-LIC-437
  - TC-FA-LIC-438
coverage:
  web: automated
---

# Role Matrix: Plan Gating per Tier Starter, Growth, Professional, dan Enterprise

## Prerequisites

- Mode: FE+BE
- Tabel "Tier yang diuji" (empat client berbeda, tiap tier punya akun Total Control sendiri):

| Tier | Akun Total Control | Pre-setup | Kredensial |
|---|---|---|---|
| Starter | `totalControlStarter_automated_{namaCompany}@qwertysystem.net` | #9 | `Spectra.env.FA_STARTER_TC_PASSWORD` |
| Growth | `totalControlGrowth_automated_{namaCompany}@qwertysystem.net` | #10 (`License allocation per group` ON) | `Spectra.env.FA_GROWTH_TC_PASSWORD` |
| Professional | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | #1 (`License allocation per group` ON) | `Spectra.env.FA_TC_PASSWORD` |
| Enterprise | `totalControlEnterprise_automated_{namaCompany}@qwertysystem.net` | #11 (`License allocation per group` ON) | `Spectra.env.FA_ENT_TC_PASSWORD` |

- Login akun pertama (Starter) di hook `before` spec ini; halaman Fixed Asset > License dibuka hook `beforeEach` suite. Tiga akun lain diganti dengan langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control Pre-setup #1).
- Data: hanya dibaca, tidak ada state yang diubah selain tanggal fixture di bawah. Data kuota, ledger Add-on, riwayat, dan sesi tiap client sudah tersedia di Pre-setup #1, #9, #10, #11 (#12, #13, #14 untuk Professional). Berkas `fixtures/` untuk Pre-setup License (`Fixture.fixedAssetLicense.*`) belum ada; disediakan tim FE.
- Banner Renewal: term live Active tiap client memakai atribut Pre-setup #15 (Plan Owner `PT Maju Bersama`, End Date 31/12/26, konfigurasi Client Lifecycle 30/7/1). Hook `before` spec ini mengatur tanggal fixture "hari ini" ke 01/12/26 (N = 30) untuk keempat client lewat fixture BE sebelum halaman dibuka, dan hook `after` mengembalikannya.
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### Tier Starter (TC-FA-LIC-435)

1. Verifikasi Tab `Allocation Quota` tidak tampil (Hidden)
2. Verifikasi Sub-Tab `Subscription History` dan `Allocation History` tidak dirender
3. Verifikasi kolom addon pada License Summary `Not Available`
4. Verifikasi baris `Unmanaged` tampil
5. Klik Tab `Concurrent User`
6. Verifikasi Tab `Concurrent User` tersedia
7. Verifikasi Banner Renewal stage Notice tampil di atas Tabs Bar
8. Verifikasi Title banner `Subscription expires in 30 days`
9. Verifikasi Body banner `Contact PT Maju Bersama to renew and keep your license and assets uninterrupted.`

### Tier Growth (TC-FA-LIC-436)

10. Ganti akun: Logout
11. Login sebagai Total Control tier Growth Pre-setup #10 (`Spectra.env.FA_GROWTH_TC_PASSWORD`)
12. Klik menu License pada sidebar
13. Verifikasi Tab `Allocation Quota` tampil
14. Verifikasi Sub-Tab `Subscription History` dan `Allocation History` dirender
15. Verifikasi kolom addon membaca ledger Add-on (`Not Available` hanya bila addon belum pernah dialokasikan)
16. Verifikasi baris `Unmanaged` tampil
17. Klik Tab `Concurrent User`
18. Verifikasi Tab `Concurrent User` tersedia
19. Verifikasi Banner Renewal stage Notice tampil di atas Tabs Bar
20. Verifikasi Title banner `Subscription expires in 30 days`
21. Verifikasi Body banner `Contact PT Maju Bersama to renew and keep your license and assets uninterrupted.`

### Tier Professional (TC-FA-LIC-437)

22. Ganti akun: Logout
23. Login sebagai Total Control tier Professional Pre-setup #1 (`Spectra.env.FA_TC_PASSWORD`)
24. Klik menu License pada sidebar
25. Verifikasi Tab `Allocation Quota` tampil
26. Verifikasi Sub-Tab `Subscription History` dan `Allocation History` dirender
27. Verifikasi kolom addon membaca ledger Add-on (`Not Available` hanya bila addon belum pernah dialokasikan)
28. Verifikasi baris `Unmanaged` tampil
29. Klik Tab `Concurrent User`
30. Verifikasi Tab `Concurrent User` tersedia
31. Verifikasi Banner Renewal stage Notice tampil di atas Tabs Bar
32. Verifikasi Title banner `Subscription expires in 30 days`
33. Verifikasi Body banner `Contact PT Maju Bersama to renew and keep your license and assets uninterrupted.`

### Tier Enterprise (TC-FA-LIC-438)

34. Ganti akun: Logout
35. Login sebagai Total Control tier Enterprise Pre-setup #11 (`Spectra.env.FA_ENT_TC_PASSWORD`)
36. Klik menu License pada sidebar
37. Verifikasi Tab `Allocation Quota` tampil
38. Verifikasi Sub-Tab `Subscription History` dan `Allocation History` dirender
39. Verifikasi kolom addon membaca ledger Add-on (`Not Available` hanya bila addon belum pernah dialokasikan)
40. Verifikasi baris `Unmanaged` tampil
41. Klik Tab `Concurrent User`
42. Verifikasi Tab `Concurrent User` tersedia
43. Verifikasi Banner Renewal stage Notice tampil di atas Tabs Bar
44. Verifikasi Title banner `Subscription expires in 30 days`
45. Verifikasi Body banner `Contact PT Maju Bersama to renew and keep your license and assets uninterrupted.`

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-435, 436, 437, 438). Tidak ada TC hanya-BE di spec ini.
- Spec ditulis per blok tier, bukan perulangan atas tabel, karena langkah tier Starter berbeda dari tiga tier lain (Hidden dan tidak dirender versus tampil) dan ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): ganti akun pada langkah 10, 11, 22, 23, 34, 35 dan membuka License pada langkah 12, 24, 36.
- Temuan untuk QA:
  - Expected butir c TC-436, 437, 438 ("kolom addon membaca ledger Add-on") tidak menyebut nilai per client; Pre-setup #10 dan #11 tidak memuat data ledger Add-on, sehingga asersi mengikuti rumusan TC.
- Alasan di atas 35 langkah (45 langkah): satu blok per tier plan (Starter, Growth, Professional, Enterprise) dengan akun dan data masing-masing; keempat blok satu topik (gating per tier) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
