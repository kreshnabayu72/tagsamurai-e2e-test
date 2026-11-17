---
id: TC-FA-FAAC-E2E-052-create-akun-sama-shortcut-create-account-dan-titik-peringatan-tab
title: "Form Create Asset Class: Titik Peringatan Tab, Shortcut Create Account, dan Akun yang Sama dengan Asset Class Lain"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-93
  - TC-FA-FAAC-94
  - TC-FA-FAAC-131
  - TC-FA-FAAC-133
sourceRules: ["ST-04", "§4.5#b3", "FI-07", "§4.4#r12", "§4.2f#b2", "T-01", "V-38", "FAAC-LOGIC-04i"]
smoke: []
dependsOn: []
trace:
  "ST-04": [3, 6, 7]
  "§4.5#b3": 4
  "FI-07": [10, 11, 13]
  "§4.4#r12": 10
  "§4.2f#b2": 15
  "T-01": [22, 33]
  "V-38": [23, 30]
  "FAAC-LOGIC-04i": [24, 30, 34]
coverage:
  web: automated
---

# Form Create Asset Class: Titik Peringatan Tab, Shortcut Create Account, dan Akun yang Sama dengan Asset Class Lain

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Asset Class `B-ANCHOR` (Active) dengan Asset Cost `11001 – Machinery Cost` tersimpan, disediakan fixture BE sebagai precondition TC-93 (tidak diubah); Chart of Accounts memuat akun Active `11001 – Machinery Cost`, `12001 – Accumulated Depreciation Machinery`, `12002 – Accumulated Depreciation Other`, `51001 – Depreciation Expense Machinery`, `51002 – Depreciation Expense Other`, dan `81001 – Gain on Disposal`; Tax Depreciation Class `Bukan bangunan – Kelompok 3` Active.
- Data yang dibuat spec (nama literal dari TC): akun Chart of Accounts kode `11999` (belum ada sebelum spec), Asset Class `B-SHARE` dan `B-GL` (belum ada sebelum spec). Hook `after` menghapus akun `11999`, `B-SHARE`, dan `B-GL` lewat fixture BE (pembersihan tidak mengandalkan setup berhasil penuh). Efek pada Chart of Accounts (akun `11999` dibuat lalu dihapus) berlaku untuk client bersama.
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (sesi API aktor, seed dan pemulihan lewat fixture BE, flag Guided Tooltip): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-133: Titik peringatan tab hilang saat field wajib terisi dan label aksesibilitas tab

1. Klik tombol `[+ Asset Class]` di toolbar tabel
2. Klik `[Submit]` tanpa mengisi apa pun
3. Verifikasi tab General dan tab Depreciation memiliki titik peringatan merah
4. Verifikasi label aksesibilitas `General, has required fields` dan `Depreciation, has required fields`
5. Pada tab General isi Class Code `B-DOT` dan Class Name `Dot`
6. Verifikasi titik peringatan pada tab General hilang
7. Verifikasi tab Depreciation tetap bertitik

### TC-FA-FAAC-131: Shortcut + Create account membuka modal Add Account dan akun baru langsung terpilih

8. Klik tab `Accounts`
9. Buka select Asset Cost lalu klik `+ Create account`
10. Verifikasi modal Add Account milik Chart of Accounts terbuka
11. Verifikasi Account Function terisi `Asset Cost` dan terkunci
12. Isi nama akun `Asset Cost Baru` dan kode `11999`, lalu simpan akun
13. Verifikasi akun `11999 – Asset Cost Baru` langsung terpilih di field Asset Cost
14. Klik breadcrumb `Asset Class`
15. Verifikasi dialog `Unsaved Changes` dengan tombol `Cancel` dan `Leave`
16. Klik `[Leave]`

### TC-FA-FAAC-93: Create kedua dengan akun yang sama seperti Asset Class lain

17. Klik tombol `[+ Asset Class]` di toolbar tabel
18. Pada tab General isi Class Code `B-SHARE`, Class Name `Shared Account Fixture`
19. Isi field lain dengan nilai valid: Method `Straight Line`, Useful Life `60`, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`
20. Pada tab Accounts pilih Asset Cost `11001 – Machinery Cost` (akun yang sama dengan `B-ANCHOR`), Accumulated Depreciation `12002 – Accumulated Depreciation Other`, Depreciation Expense `51002 – Depreciation Expense Other`
21. Klik `[Submit]`
22. Verifikasi toast sukses `Success, asset class has been created.`
23. Verifikasi tidak ada caption error pada field akun
24. Verifikasi akun `11001 – Machinery Cost` dipakai dua Asset Class (`B-ANCHOR` dan `B-SHARE`)

### TC-FA-FAAC-94: Create dengan akun Gain on Disposal dan Loss on Disposal yang sama

25. Klik breadcrumb `Asset Class` untuk kembali ke tabel
26. Klik tombol `[+ Asset Class]` di toolbar tabel
27. Pada tab General isi Class Code `B-GL`, Class Name `Gain Loss Fixture`
28. Isi field lain dengan nilai valid: Method `Straight Line`, Useful Life `60`, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`
29. Pada tab Accounts pilih Gain on Disposal `81001 – Gain on Disposal` dan pilih akun yang sama `81001 – Gain on Disposal` pada Loss on Disposal
30. Verifikasi select Loss on Disposal menerima akun ber-function Gain on Disposal tanpa caption konflik akun
31. Pilih Asset Cost `11001 – Machinery Cost`, Accumulated Depreciation `12001 – Accumulated Depreciation Machinery`, Depreciation Expense `51001 – Depreciation Expense Machinery`
32. Klik `[Submit]`
33. Verifikasi toast sukses `Success, asset class has been created.`
34. Verifikasi pasangan Gain on Disposal dan Loss on Disposal tersimpan memakai akun yang sama `81001 – Gain on Disposal`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-93, 94, 131, 133). Tidak ada TC hanya-BE di spec ini.
- Pengecualian beralasan atas S-06 dan S-12: Class Code, Class Name, dan kode akun literal dari TC dipakai apa adanya tanpa suffix `{runId}-<NNN>` karena asersi TC bergantung pada nama; seed idempotent per spec oleh fixture BE (keputusan yang disetujui user).
- Urutan TC diubah dari urutan nomor: TC-133 (validasi diblokir) lebih dulu, TC-131 melanjutkan form Create yang sama sehingga langkah membuka form TC-131 (`[+ Asset Class]`) tidak diulang, form ditutup sekali di langkah 14 sampai 16, baru TC-93 dan TC-94 (aksi sukses) (S-10).
- Spec ini sekitar 34 langkah. Langkah penghubung (aksi tanpa `Verifikasi`, bukan asersi TC): langkah 14 dan 16 (menutup form dirty; langkah 15 `Verifikasi` dialog diwajibkan S-08), langkah 25 (kembali ke tabel lewat breadcrumb), langkah 8 (TC-131 mulai dari form Create yang masih terbuka).
- Langkah 22 menjadi anchor positif untuk asersi absence pada langkah 23.
- Temuan untuk QA:
  - TC-93 Expected b ("akun dipakai dua Asset Class") tidak punya langkah observasi di TC; langkah 24 mengasersinya sebagai kesimpulan dari Submit sukses dengan akun yang sama seperti `B-ANCHOR`.
  - TC-94 menyebut "tiga akun berbeda" untuk Asset Cost, Accumulated Depreciation, dan Depreciation Expense tanpa menyebut akunnya; spec memakai `11001`, `12001`, dan `51001` dari data Pre-setup.
  - TC-94 menyebut "tanpa caption V-38" tanpa teks caption; langkah 30 mengasersi ketiadaan caption konflik akun (`Account already used for ...`) pada select Loss on Disposal.
  - TC-131 Post Condition ("Akun 11999 tersimpan di Chart of Accounts") tidak punya langkah observasi di TC, jadi tidak diasersi; akun dihapus hook `after`. TC-131 tidak menyebut Class Name yang diisi pada form Create sebelum shortcut; spec melanjutkan form TC-133 (`B-DOT` dan `Dot`).
