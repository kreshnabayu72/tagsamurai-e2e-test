---
id: TC-FA-BORROW-UI-069-empty-state-dan-loading
title: "State kosong, loading, dan gagal muat surface Borrow"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["S-BRW-01", "S-BRW-02", "S-BRW-03", "S-BRW-04", "S-BRW-05", "S-BRW-06", "S-BRW-07", "S-BRW-08", "S-BRW-09", "S-BRW-10", "S-BRW-11", "S-BRW-12", "S-BRW-13"]
smoke: []
dependsOn: []
trace:
  "S-BRW-01": [2, 4]
  "S-BRW-02": [6, 8]
  "S-BRW-03": [10, 12]
  "S-BRW-04": [14, 16]
  "S-BRW-05": [18, 20]
  "S-BRW-06": [22, 24]
  "S-BRW-07": [26, 27]
  "S-BRW-08": [29, 31]
  "S-BRW-09": [33, 34, 37, 39]
  "S-BRW-10": [41, 43, 45, 47, 49, 51, 53]
  "S-BRW-11": 55
  "S-BRW-12": 57
  "S-BRW-13": [59, 61]
anchor: []
coverage:
  web: automated
---

# State kosong, loading, dan gagal muat surface Borrow

## Prerequisites
- Aktor: Aktor Borrow dengan cakupan Group `Finance`.
- Layar awal: Halaman Borrow dan surface turunannya
- Komponen: Surface kosong Borrow
- Data:
  - DU-069-1: BRW `BRW-2026-0153` pada tabel Transactions.
  - DU-069-2: tanggal hari ini `18/11/2026` dan rentang default tab History `20/08/2026` sampai `18/11/2026`.
  - DU-069-3: rentang filter Last Updated yang diisi pengguna, `01/01/2026` sampai `31/01/2026`.
- Kondisi:
  - K1: tab Transactions tanpa data dan tanpa filter.
  - K2: tab Transactions dengan filter atau pencarian yang tidak menghasilkan baris.
  - K3: tab Borrowed Assets tanpa data dan tanpa filter.
  - K4: tab Borrowed Assets dengan filter atau pencarian yang tidak menghasilkan baris.
  - K5: tab History tanpa data dan tanpa filter.
  - K6: tab History dengan filter atau pencarian yang tidak menghasilkan baris.
  - K7: tab Drafts tanpa data dan tanpa filter.
  - K8: tab Drafts dengan filter atau pencarian yang tidak menghasilkan baris.
  - K9: tab Approvals > Borrow Active tanpa data dan tanpa filter.
  - K10: tab Approvals > Borrow Active dengan filter atau pencarian yang tidak menghasilkan baris.
  - K11: tab Approvals > Borrow History tanpa data dan tanpa filter.
  - K12: tab Approvals > Borrow History dengan filter atau pencarian yang tidak menghasilkan baris.
  - K13: tabel Transactions sedang dimuat, lalu pemuatan selesai dengan baris `BRW-2026-0153`.
  - K14: pemuatan tabel Transactions gagal, lalu pemuatan ulang berhasil dengan baris `BRW-2026-0153`.
  - K15: Date Format bernilai `DD/MM/YYYY`, tanggal hari ini `18/11/2026`, filter Last Updated tab History bernilai rentang default 90 hari terakhir `20/08/2026` sampai `18/11/2026`, dan semua baris lebih lama dari rentang itu.
  - K16: tabel Assets pada Borrow Detail dengan filter atau pencarian yang tidak menghasilkan baris.
  - K17: tabel T-BRW-08 pada halaman Review Approval dengan filter atau pencarian yang tidak menghasilkan baris.
  - K18: tabel pada halaman Review Extension Request dengan filter atau pencarian yang tidak menghasilkan baris.
  - K19: detail Borrowed Asset dengan filter atau pencarian yang tidak menghasilkan baris.
  - K20: dialog Select Asset tabel T-BRW-02 dengan filter atau pencarian yang tidak menghasilkan baris.
  - K21: dialog Select Asset tabel T-BRW-04 dengan filter atau pencarian yang tidak menghasilkan baris.
  - K22: dialog tabel T-BRW-05 dengan filter atau pencarian yang tidak menghasilkan baris.
  - K23: Select Borrower tanpa Borrower.
  - K24: dialog Select Asset tanpa aset eligible.
  - K25: detail Borrowed Asset tanpa aset yang dipegang Borrower.
  - K26: pemuatan detail Borrowed Asset gagal.

## Test Steps

### Empty state tab Transactions tanpa data
1. Tampilkan Surface kosong Borrow dengan kondisi K1
2. Verifikasi empty state menampilkan `No borrows yet` dan `Borrowed assets will appear here.`

### Empty state tab Transactions akibat filter
3. Tampilkan Surface kosong Borrow dengan kondisi K2
4. Verifikasi empty state menampilkan `No results found` dan `Try adjusting your search or filter.`

### Empty state tab Borrowed Assets tanpa data
5. Tampilkan Surface kosong Borrow dengan kondisi K3
6. Verifikasi empty state menampilkan `No assets are out right now` dan `Borrowed assets will appear here after handover.`

### Empty state tab Borrowed Assets akibat filter
7. Tampilkan Surface kosong Borrow dengan kondisi K4
8. Verifikasi empty state menampilkan `No results found` dan `Try adjusting your search or filter.`

### Empty state tab History tanpa data
9. Tampilkan Surface kosong Borrow dengan kondisi K5
10. Verifikasi empty state menampilkan `No finished borrows yet` dan `Returned, rejected, and canceled borrows will appear here.`

### Empty state tab History akibat filter
11. Tampilkan Surface kosong Borrow dengan kondisi K6
12. Verifikasi empty state menampilkan `No results found` dan `Try adjusting your search or filter.`

### Empty state tab Drafts tanpa data
13. Tampilkan Surface kosong Borrow dengan kondisi K7
14. Verifikasi empty state menampilkan `No drafts` dan `Saved drafts from you and your team will appear here.`

### Empty state tab Drafts akibat filter
15. Tampilkan Surface kosong Borrow dengan kondisi K8
16. Verifikasi empty state menampilkan `No results found` dan `Try adjusting your search or filter.`

### Empty state tab Approvals > Borrow Active tanpa data
17. Tampilkan Surface kosong Borrow dengan kondisi K9
18. Verifikasi empty state menampilkan `No pending approvals` dan `You have no pending approval requests at this moment.`

### Empty state tab Approvals > Borrow Active akibat filter
19. Tampilkan Surface kosong Borrow dengan kondisi K10
20. Verifikasi empty state menampilkan `No results found` dan `Try adjusting your search or filter.`

### Empty state tab Approvals > Borrow History tanpa data
21. Tampilkan Surface kosong Borrow dengan kondisi K11
22. Verifikasi empty state menampilkan `No history yet` dan `Decided or closed borrows will appear here.`

### Empty state tab Approvals > Borrow History akibat filter
23. Tampilkan Surface kosong Borrow dengan kondisi K12
24. Verifikasi empty state menampilkan `No results found` dan `Try adjusting your search or filter.`

### Loading memakai Shimmer
25. Tampilkan Surface kosong Borrow dengan kondisi K13
26. Verifikasi isi tabel Transactions belum terbaca selama pemuatan berlangsung
27. Verifikasi baris `BRW-2026-0153` terbaca sesudah pemuatan selesai

### Gagal muat dan Try Again
28. Tampilkan Surface kosong Borrow dengan kondisi K14
29. Verifikasi pesan `Unable to load this data.` dan tombol `[Try Again]` tampil
30. Klik `[Try Again]`
31. Verifikasi baris `BRW-2026-0153` tampil sesudah pemuatan ulang berhasil

### Rentang default tab History
32. Tampilkan Surface kosong Borrow dengan kondisi K15
33. Verifikasi empty state menampilkan `No results found` dan `Try adjusting your search or filter.` pada tab History karena rentang default
34. Verifikasi filter Last Updated menampilkan rentang `20/08/2026` sampai `18/11/2026`
35. Ganti filter Last Updated dengan rentang `01/01/2026` sampai `31/01/2026`
36. Klik `[Clear Field]`
37. Verifikasi filter Last Updated kembali menampilkan rentang default `20/08/2026` sampai `18/11/2026`, bukan tanpa rentang
38. Kosongkan field tanggal filter Last Updated
39. Verifikasi field tanggal filter Last Updated kosong

### Kosong akibat filter pada tabel Assets pada Borrow Detail
40. Tampilkan Surface kosong Borrow dengan kondisi K16
41. Verifikasi empty state menampilkan `No results found` dan `Try adjusting your search or filter.`

### Kosong akibat filter pada tabel T-BRW-08 pada halaman Review
42. Tampilkan Surface kosong Borrow dengan kondisi K17
43. Verifikasi empty state menampilkan `No results found` dan `Try adjusting your search or filter.`

### Kosong akibat filter pada tabel Review Extension Request
44. Tampilkan Surface kosong Borrow dengan kondisi K18
45. Verifikasi empty state menampilkan `No results found` dan `Try adjusting your search or filter.`

### Kosong akibat filter pada detail Borrowed Asset
46. Tampilkan Surface kosong Borrow dengan kondisi K19
47. Verifikasi empty state menampilkan `No results found` dan `Try adjusting your search or filter.`

### Kosong akibat filter pada dialog tabel T-BRW-02
48. Tampilkan Surface kosong Borrow dengan kondisi K20
49. Verifikasi empty state menampilkan `No results found` dan `Try adjusting your search or filter.`

### Kosong akibat filter pada dialog tabel T-BRW-04
50. Tampilkan Surface kosong Borrow dengan kondisi K21
51. Verifikasi empty state menampilkan `No results found` dan `Try adjusting your search or filter.`

### Kosong akibat filter pada dialog tabel T-BRW-05
52. Tampilkan Surface kosong Borrow dengan kondisi K22
53. Verifikasi empty state menampilkan `No results found` dan `Try adjusting your search or filter.`

### Select Borrower tanpa data
54. Tampilkan Surface kosong Borrow dengan kondisi K23
55. Verifikasi opsi Select Borrower menampilkan `No borrowers found` dan `Borrowers will appear here.`

### Select Asset tanpa data
56. Tampilkan Surface kosong Borrow dengan kondisi K24
57. Verifikasi dialog Select Asset menampilkan `No assets found` dan `Eligible assets will appear here.`

### Borrowed Asset detail tanpa aset
58. Tampilkan Surface kosong Borrow dengan kondisi K25
59. Verifikasi detail Borrowed Asset menampilkan `No borrowed assets` dan `Assets held by this borrower will appear here.`

### Gagal muat pada detail Borrowed Asset
60. Tampilkan Surface kosong Borrow dengan kondisi K26
61. Verifikasi detail Borrowed Asset menampilkan `Unable to load this data.` dan tombol `[Try Again]`
