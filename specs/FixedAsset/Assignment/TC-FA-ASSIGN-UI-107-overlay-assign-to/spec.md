---
id: TC-FA-ASSIGN-UI-107-overlay-assign-to
title: "Overlay Assign to: pilih tipe Assignee"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-ASG-23, "§4.1#r14"]
smoke: []
dependsOn: []
trace:
  D-ASG-23: [3, 4, 5, 6, 11, 12, 16, 17, 21, 22, 25, 29]
  "§4.1#r14": 7
anchor: [28]
coverage:
  web: automated
---
# Overlay Assign to: pilih tipe Assignee

## Prerequisites
- Aktor: Asset Admin pada Group `Head Office`.
- Layar awal: halaman Assignment, tab Transactions untuk K1 dan K3; tab Drafts untuk K2.
- Komponen: Overlay Assign to
- Kondisi:
  - K1: level Full; tab Transactions aktif.
  - K2: level Full; tab Drafts aktif.
  - K3: level Basic; tab Transactions aktif.

## Test Steps

### Overlay dibuka dari tab Transactions: judul, dua pilihan, dan Cancel
1. Tampilkan Overlay Assign to dengan kondisi K1
2. Klik `[+ Assign]`
3. Verifikasi overlay `Assign to` tampil
4. Verifikasi pilihan `Employee` memuat teks `Assign to one employee who can sign in.`
5. Verifikasi pilihan `Division` memuat teks `Assign to a division with one PIC.`
6. Verifikasi overlay memuat tombol `[Cancel]`
7. Verifikasi overlay memuat tepat dua pilihan, yaitu `Employee` dan `Division`

### Memilih Employee menutup overlay dan membuka form dengan Assignee Type Employee
8. Tampilkan Overlay Assign to dengan kondisi K1
9. Klik `[+ Assign]`
10. Klik pilihan `Employee`
11. Verifikasi overlay `Assign to` tertutup
12. Verifikasi form Assignment Request terbuka dengan Assignee Type `Employee`

### Memilih Division menutup overlay dan membuka form dengan Assignee Type Division
13. Tampilkan Overlay Assign to dengan kondisi K1
14. Klik `[+ Assign]`
15. Klik pilihan `Division`
16. Verifikasi overlay `Assign to` tertutup
17. Verifikasi form Assignment Request terbuka dengan Assignee Type `Division`

### Cancel menutup overlay tanpa membuka form
18. Tampilkan Overlay Assign to dengan kondisi K1
19. Klik `[+ Assign]`
20. Klik `[Cancel]`
21. Verifikasi overlay `Assign to` tertutup
22. Verifikasi form Assignment Request tidak terbuka

### Overlay juga tersedia dari tab Drafts
23. Tampilkan Overlay Assign to dengan kondisi K2
24. Klik `[+ Assign]`
25. Verifikasi overlay `Assign to` tampil dengan pilihan `Employee` dan `Division`

### Level Basic tidak menampilkan overlay
26. Tampilkan Overlay Assign to dengan kondisi K3
27. Klik `[+ Assign]`
28. Verifikasi form Assignment Request terbuka dengan Assignee Type `Employee`
29. Verifikasi overlay `Assign to` tidak tampil
