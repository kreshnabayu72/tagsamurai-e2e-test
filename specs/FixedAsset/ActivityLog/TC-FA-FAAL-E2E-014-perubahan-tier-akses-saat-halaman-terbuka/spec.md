---
id: TC-FA-FAAL-E2E-014-perubahan-tier-akses-saat-halaman-terbuka
title: "Perubahan Tier Akses: Dicabut dan Dipromosikan saat Halaman Terbuka"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAL-55
  - TC-FA-FAAL-56
coverage:
  web: automated
---

# Perubahan Tier Akses: Dicabut dan Dipromosikan saat Halaman Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun yang dipakai:

  | Peran dalam spec | Pre-setup | Email | Env var password |
  |---|---|---|---|
  | User target pencabutan tier (Read Only), sesi UI | #9 | `readOnlyRevokeTarget_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_REVOKE_PASSWORD` |
  | User target promosi (Group Manager untuk group Gedung A), sesi UI | #8 | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |
  | Admin Total Control lain (Admin Alpha), sesi API | #1 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
- Login akun aktor pertama (user target #9) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log). Hook `after` memulihkan tier akses #8 (Group Manager) dan #9 (Read Only), lalu mengembalikan sesi UI ke akun default suite (Total Control, Pre-setup #1). Ganti akun di tengah spec memakai satu langkah logout dan login eksplisit.
- Sesi API aktor (butir "Sesi API aktor" di `suite.md`): admin Alpha (#1) mencabut dan meng-assign tingkat akses lewat sesi API yang tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE.
- Env var `FA_RO_REVOKE_PASSWORD`, `FA_GM_PASSWORD`, `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (R-07). Password tidak ditulis di spec atau fixture.
- Data: Tab User Action UA-01 sampai UA-15 (Pre-setup #12, total 15 baris), dipulihkan ke keadaan Pre-setup sebelum spec (disediakan tim FE/BE).
- State global yang diubah spec: tier akses user #8 dan #9. Pemulihan lewat langkah penghubung di akhir tiap blok TC dan hook `after`.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk akun #8 dan #9.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nilai data ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-55: Tier akses dicabut saat halaman Activity Log terbuka

1. Klik tab User Action
2. Pada sesi API admin Total Control (#1), cabut tingkat akses Read Only user target (#9) hingga tersimpan
3. Klik `Next` pada Pagination
4. Verifikasi user target: toast error "You don't have permission to do this."
5. Verifikasi user target: UI di-refresh
6. Verifikasi user target: data log tidak tampil
7. Buka sidebar Fixed Asset
8. Verifikasi user target: item menu Dashboard tetap tampil di sidebar
9. Verifikasi user target: menu `Activity Log` tidak lagi tampil di sidebar
10. Pada sesi API admin Total Control (#1), assign kembali tingkat akses Read Only ke user target (#9) hingga tersimpan

### TC-FA-FAAL-56: Group Manager dipromosikan menjadi Read Only dan memperoleh akses

11. Ganti akun: Logout dari user target #9, lalu Login sebagai Group Manager (`groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_GM_PASSWORD`) dan buka Fixed Asset > Dashboard
12. Buka sidebar Reports & Logs
13. Verifikasi Group Manager sebelum promosi: item menu Dashboard tampil di sidebar
14. Verifikasi Group Manager sebelum promosi: menu `Activity Log` Hidden
15. Pada sesi API admin Total Control (#1), assign tingkat akses Read Only ke user target (#8) hingga tersimpan
16. Muat ulang halaman
17. Buka sidebar Reports & Logs
18. Verifikasi user target setelah promosi dan muat ulang: menu `Activity Log` tampil
19. Klik `Activity Log`
20. Verifikasi user target: tab Session dapat dibuka dan menampilkan tabel
21. Klik tab User Action
22. Verifikasi user target: tab User Action dapat dibuka dan menampilkan tabel
23. Verifikasi user target: seluruh baris client tampil di Tab User Action
24. Pada sesi API admin Total Control (#1), kembalikan tingkat akses user target (#8) menjadi Group Manager hingga tersimpan

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pelaku kedua (admin Total Control lain) memakai sesi API; bukan konteks kedua kelas c (bagian 3 prinsip 13, P-2 keputusan 2026-10-30), jadi tidak memakai butir `P-2`. Sesi UI hanya satu per langkah dan berganti akun secara eksplisit (S-07).
- Langkah penghubung (S-03): langkah 1 (membuka tab User Action sebagai precondition TC-FA-FAAL-55), langkah 7, 12, dan 17 (observasi sidebar), langkah 8 dan 13 (anchor positif item menu Dashboard untuk absence menu `Activity Log`, klausa "item menu Dashboard tetap tampil" Expected b TC-FA-FAAL-55 dan a TC-FA-FAAL-56), langkah 10 dan 24 (pemulihan tier lewat sesi API), langkah 11 (ganti akun, lalu membuka Fixed Asset > Dashboard), langkah 16 (muat ulang yang diminta TC langkah 3).
- Langkah 2 dan 15 memicu perubahan state lewat sesi API dan ditulis "... hingga ... tersimpan" (R-20).
- Langkah 3: TC-FA-FAAL-55 langkah 3 menawarkan dua pilihan ("klik `Next` pada Pagination atau klik tab Session"); spec memilih `Next` pada Pagination (total 15 baris menghasilkan halaman 2).
- Langkah 5 dan 6 memecah langkah 4 sesuai klausa Expected butir a (toast, UI di-refresh, data log tidak tampil). Anchor asersi absence data log (bagian 8b butir 2): toast penolakan pada langkah 4. Anchor langkah 9 dan 14 (absence menu): Verifikasi item menu Dashboard tampil pada langkah 8 dan 13.
- Langkah 23: seluruh baris client untuk Tab User Action diasersi tanpa angka total karena TC-FA-FAAL-56 Expected butir b tidak menyebutnya; Tab Session tidak diasersi jumlahnya karena TC-FA-FAAL-56 tidak menyebut Pre-setup #11 (lihat Temuan untuk QA).
- Temuan untuk QA:
  - TC-FA-FAAL-55 dan 56 tidak menyebut env var password; nama env var diusulkan dari butir "Env var" di `suite.md`.
  - TC-FA-FAAL-56 Expected butir b menyebut "seluruh baris client" tanpa menyebut Pre-setup #11; jumlah baris Tab Session tidak diasersi.
  - TC-FA-FAAL-55 dan 56 tidak memiliki Post Condition untuk pemulihan tier. Pemulihan di langkah 10 dan 24 adalah langkah penghubung spec.
