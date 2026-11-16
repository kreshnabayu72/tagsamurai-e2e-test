---
id: TC-FA-TDC-E2E-038-batas-master-data-count-limit-inactive-ikut-dihitung-dan-berlaku-di-semua-plan
title: "Batas Master Data Count Limit: Class Inactive Ikut Dihitung dan Batas Berlaku pada Plan Growth, Professional, dan Enterprise"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-131
  - TC-FA-TDC-759
  - TC-FA-TDC-760
  - TC-FA-TDC-761
  - TC-FA-TDC-762
sourceRules: ["D-07", "F-FATDC-01.k9", "FATDC-LOGIC-13b", "FATDC-LOGIC-13a"]
smoke: []
dependsOn: []
trace:
  "D-07": [2, 8, 14]
  "F-FATDC-01.k9": [3, 9, 15]
  "FATDC-LOGIC-13b": 8
  "FATDC-LOGIC-13a": 14
coverage:
  web: automated
---

# Batas Master Data Count Limit: Class Inactive Ikut Dihitung dan Batas Berlaku pada Plan Growth, Professional, dan Enterprise

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control pada company uji khusus automation. Akun, email, dan company tidak tertulis di TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan tim FE).
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data uji (kelas e, volume data; kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): company pada plan Growth; Master Data Count Limit di Admin Console > Plans & Licensing > Lifecycle Settings > System Limits bernilai 1000 (nilai minimum) dan total Tax Depreciation Class (semua status) = 1000, yaitu 7 class seed bawaan ditambah 993 class tambahan yang dibuat lewat API pre-setup di hook `before`; salah satu class tambahan adalah NB-OLD (Active di awal spec). Total 1000 berasal dari seeding (8b.10).
- Tabel "Plan uji" (parameter pada TC-FA-TDC-759 sampai 762; plan diatur lewat fixture BE): Growth untuk TC-FA-TDC-760, Professional untuk TC-FA-TDC-761, Enterprise untuk TC-FA-TDC-762. TC-FA-TDC-759 berjalan pada plan Growth awal company uji (TC tidak menyebut plan).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): mengatur Master Data Count Limit, membuat 993 class tambahan, mengatur plan client (Growth, Professional, Enterprise), dan mengatur status NB-OLD menjadi Inactive lewat fixture BE.
- State global: Master Data Count Limit, plan company, dan 993 class tambahan. Hook `after` menghapus 993 class tambahan, memulihkan NB-OLD dan plan ke Growth, dan memulihkan Master Data Count Limit ke nilai awal.
- Rujukan suite: `suite.md` (hook `before`, `beforeEach`, `after`; seed dan pemulihan lewat API).

## Test Steps

### TC-FA-TDC-759: Master Data Count Limit menjadi batas jumlah class

1. Klik `+ Class` di toolbar tab Tax Depreciation Class
2. Verifikasi dialog blok berjudul "Tax Depreciation Class Limit Reached" tampil dengan teks "You've reached the platform limit of 1000 records. Contact support if you need a higher limit." dan tombol `[OK]`
3. Verifikasi Drawer Create tidak terbuka
4. Klik `[OK]` pada dialog

### TC-FA-TDC-760, TC-FA-TDC-761, TC-FA-TDC-762: Batas berlaku per plan

Untuk setiap plan pada tabel "Plan uji" di Prerequisites (langkah 5 sampai 10):

5. Atur plan client ke plan tersebut lewat fixture BE hingga tersimpan
6. Muat ulang halaman dengan F5
7. Klik `+ Class` di toolbar tab Tax Depreciation Class
8. Verifikasi dialog blok berjudul "Tax Depreciation Class Limit Reached" tampil dengan teks "You've reached the platform limit of 1000 records. Contact support if you need a higher limit." dan tombol `[OK]`
9. Verifikasi Drawer Create tidak terbuka
10. Klik `[OK]` pada dialog

### TC-FA-TDC-131: Class Inactive ikut dihitung

11. Atur NB-OLD menjadi Inactive lewat fixture BE sehingga total 1000 terdiri atas 999 Active dan 1 Inactive hingga tersimpan
12. Muat ulang halaman dengan F5
13. Klik `+ Class`
14. Verifikasi dialog D-07 muncul
15. Verifikasi Drawer tidak terbuka
16. Klik `[OK]` pada dialog D-07

## Notes

- Langkah 5 sampai 10 diulang tiga kali (Growth, Professional, Enterprise); parameter tiap iterasi ada di tabel "Plan uji" (8b.7). Ekspansi: 28 langkah (4 langkah TC-FA-TDC-759, 18 langkah perulangan, 6 langkah TC-FA-TDC-131).
- Langkah penghubung (S-03): langkah 4, 10, dan 16 menutup dialog D-07; langkah 5, 6, 11, dan 12 membentuk precondition plan dan status NB-OLD lewat fixture BE.
- TC-FA-TDC-130 dan TC-FA-TDC-133 (slot terakhir dan Stay on this form) ada di spec 232 karena membutuhkan total class 999 dan 998.
- Post Condition TC-FA-TDC-126 sampai 133 dan 759 sampai 762 tidak memiliki langkah observasi dan tidak diasersi (S-01).
- Temuan untuk QA:
  - TC tidak menyebut akun, email, dan company Total Control.
  - TC-FA-TDC-759 tidak menyebut plan company; spec memakai plan Growth awal (identik dengan TC-FA-TDC-760).
  - TC-FA-TDC-131 menyebut "999 Active + 1 Inactive (NB-OLD)" sedangkan seed bawaan modul berisi 7 class tanpa NB-OLD; spec membentuk keadaan itu lewat fixture BE.
