---
id: TC-FA-FAAL-E2E-009-role-matrix-visibilitas-menu-activity-log
title: "Role Matrix: Visibilitas Menu Activity Log (Total Control, Read Only, Default User)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-37
  - TC-FA-FAAL-38
  - TC-FA-FAAL-39
coverage:
  web: automated
---

# Role Matrix: Visibilitas Menu Activity Log (Total Control, Read Only, Default User)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

  | TC | Role | Pre-setup | Email | Env var password |
  |---|---|---|---|---|
  | TC-FA-FAAL-37 | Total Control | #1 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
  | TC-FA-FAAL-38 | Read Only | #2 | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
  | TC-FA-FAAL-39 | Default User | #3 | `defaultUserFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` |
- Login akun aktor pertama (Total Control, Pre-setup #1) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Pengecualian atas `suite.md`: precondition ketiga TC adalah Fixed Asset > Dashboard, sehingga hook `beforeEach` membuka Fixed Asset > Dashboard (bukan Activity Log) untuk spec ini. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Ganti akun di tengah spec memakai satu langkah logout dan login eksplisit.
- Env var `FA_TC_PASSWORD`, `FA_RO_PASSWORD`, `FA_DU_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (R-07). Password tidak ditulis di spec atau fixture.
- Data: spec hanya membuka halaman Activity Log dan tidak memakai baris log tertentu; tabel boleh berisi log apa pun.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk ketiga akun aktor.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas akun Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-37: Menu Activity Log tampil untuk Total Control dengan kedua tab

1. Buka sidebar Reports & Logs
2. Klik `Activity Log`
3. Verifikasi Total Control: menu `Activity Log` tampil di bawah Reports & Logs
4. Verifikasi Total Control: halaman Activity Log terbuka
5. Verifikasi Total Control: tab `Session` dan `User Action` tampil
6. Verifikasi Total Control: tabel, Filter, Search, dan Download tampil pada tab yang terbuka
7. Klik tab User Action
8. Verifikasi Total Control: tabel, Filter, Search, dan Download tampil pada tab User Action

### TC-FA-FAAL-38: Menu Activity Log tampil untuk Read Only dengan kedua tab

9. Ganti akun: Logout dari akun Total Control, lalu Login sebagai Read Only (`readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_RO_PASSWORD`) dan buka Fixed Asset > Dashboard
10. Buka sidebar Reports & Logs
11. Klik `Activity Log`
12. Verifikasi Read Only: menu `Activity Log` tampil di bawah Reports & Logs
13. Verifikasi Read Only: halaman Activity Log terbuka
14. Verifikasi Read Only: tab `Session` dan `User Action` tampil
15. Verifikasi Read Only: tabel tampil pada tab yang terbuka
16. Verifikasi Read Only: Filter, Search, dan Download tampil dan aktif pada tab yang terbuka
17. Klik tab User Action
18. Verifikasi Read Only: tabel tampil pada tab User Action
19. Verifikasi Read Only: Filter, Search, dan Download tampil dan aktif pada tab User Action

### TC-FA-FAAL-39: Menu Activity Log tampil untuk Default User

20. Ganti akun: Logout dari akun Read Only, lalu Login sebagai Default User (`defaultUserFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_DU_PASSWORD`) dan buka Fixed Asset > Dashboard
21. Buka sidebar Reports & Logs
22. Klik `Activity Log`
23. Verifikasi Default User: menu `Activity Log` tampil di bawah Reports & Logs
24. Verifikasi Default User: halaman Activity Log terbuka dengan tab `Session` dan `User Action`
25. Verifikasi Default User: tabel, Filter, Search, dan Download tampil pada tab yang terbuka
26. Klik tab User Action
27. Verifikasi Default User: tabel, Filter, Search, dan Download tampil pada tab User Action

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec Role Matrix visibilitas (bagian 3a): satu daftar elemen, banyak role. Spec ditulis per blok role karena ganti akun menuntut langkah eksplisit (akun pertama login di hook `before`, S-07); tiap blok berdiri sendiri.
- Langkah penghubung (S-03): langkah 9 dan 20 (ganti akun, lalu membuka Fixed Asset > Dashboard sebagai precondition TC berikutnya).
- Langkah 3 dan 4 dipisah (menu tampil, halaman terbuka) karena Expected butir a TC memuat dua klausa. Pada langkah 6, 15 dan seterusnya "tab yang terbuka" adalah tab awal halaman; tab lainnya diperiksa setelah klik tab User Action (langkah 7 dan seterusnya) agar kata "di kedua tab" pada Expected butir b terpenuhi.
- Keterangan dalam kurung pada Expected TC-FA-FAAL-39 butir b ("Default User setara Total Control") adalah alasan, bukan klausa terpisah, sehingga tidak punya `Verifikasi` sendiri.
- Temuan untuk QA:
  - TC-FA-FAAL-37 sampai 39 tidak menyebut tab awal yang terbuka saat Activity Log dibuka; spec memverifikasi tab yang terbuka lalu tab User Action. Kedua tab tercakup hanya bila tab awal adalah Session.
  - TC-FA-FAAL-37 sampai 39 tidak menyebut env var password; nama env var diusulkan dari butir "Env var" di `suite.md`.
