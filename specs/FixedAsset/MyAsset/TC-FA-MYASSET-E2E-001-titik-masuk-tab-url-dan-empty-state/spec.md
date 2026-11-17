---
id: TC-FA-MYASSET-E2E-001-titik-masuk-tab-url-dan-empty-state
title: "Titik masuk My Asset dari menu profil, tab awal Task, tab di URL, dan empty state tiap tab"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§1.2#r20", "§1.2#r21", "§1.2#r22", "§3#p2", "§4.1#r1", "§4.3#r3", "§4.4#r1", "§4.4#r45", "§4.4#r46", "§7.1#r1", "§7.1#r2", "§7.1#r3", "§7.1#r4", "§9.4.2#r2", "§9.4.2#r13", "§10#r2"]
smoke: []
dependsOn: []
trace:
  "§1.2#r20": 11
  "§1.2#r21": [15, 19, 23, 27, 29, 31, 33]
  "§1.2#r22": [29, 31, 33, 35, 37]
  "§3#p2": [10, 11]
  "§4.1#r1": [6, 7]
  "§4.3#r3": 8
  "§4.4#r1": [11, 15, 19, 23, 27]
  "§4.4#r45": [15, 19, 23, 27]
  "§4.4#r46": [29, 31, 33]
  "§7.1#r1": [12, 13]
  "§7.1#r2": [16, 17]
  "§7.1#r3": [20, 21]
  "§7.1#r4": [24, 25]
  "§9.4.2#r2": [11, 12, 13]
  "§9.4.2#r13": [12, 13, 16, 17, 20, 21, 24, 25]
  "§10#r2": [2, 4, 8]
anchor: [1, 3]
coverage:
  web: automated
---

# Titik masuk My Asset dari menu profil, tab awal Task, tab di URL, dan empty state tiap tab

## Prerequisites
- Aktor: Borrower tanpa pinjaman dan tanpa penugasan.
- Layar awal: halaman FAMS yang memuat navbar dan sidebar.
- Data:
  - DU-001-1: User `Rina Wulandari {runId}`, sebagai Borrower tanpa Task aktif, tanpa pinjaman, tanpa penugasan, dan tanpa riwayat, dengan flag Guided Tooltip My Asset sudah disetel (tur sudah pernah dilihat). Baris pinjaman atau penugasan milik pengguna lain di entitas yang sama bukan miliknya.

## Test Steps

### Avatar dan sidebar tanpa pengingat atau grup My Asset
1. Verifikasi avatar di navbar tampil
2. Verifikasi tidak ada badge atau titik pengingat pada avatar
3. Verifikasi sidebar tampil
4. Verifikasi tidak ada grup `My Asset` di sidebar

### Item My Asset di menu profil tanpa pengingat
5. Klik avatar di navbar
6. Verifikasi item `My Asset` tampil di menu profil
7. Verifikasi menu profil memuat item akun lain di samping item `My Asset`
8. Verifikasi tidak ada badge atau titik pengingat pada item `My Asset`

### Titik masuk membuka tab Task dengan empty state
9. Klik item `My Asset`
10. Verifikasi halaman `My Asset` terbuka
11. Verifikasi tab `Task` terbuka sebagai tab awal
12. Verifikasi empty state tab `Task` menampilkan judul `No tasks`
13. Verifikasi empty state tab `Task` menampilkan deskripsi `Handover confirmations appear here.`

### Tab Borrowed tersimpan di URL dan kosong
14. Klik tab `Borrowed`
15. Verifikasi URL memuat parameter `?tab=` bernilai `borrowed`
16. Verifikasi empty state tab `Borrowed` menampilkan judul `You're not borrowing anything`
17. Verifikasi empty state tab `Borrowed` menampilkan deskripsi `Assets you borrow will appear here.`

### Tab Assigned tersimpan di URL dan kosong
18. Klik tab `Assigned`
19. Verifikasi URL memuat parameter `?tab=` bernilai `assigned`
20. Verifikasi empty state tab `Assigned` menampilkan judul `No assets are assigned to you`
21. Verifikasi empty state tab `Assigned` menampilkan deskripsi `Assets assigned to you will appear here.`

### Tab History tersimpan di URL dan kosong
22. Klik tab `History`
23. Verifikasi URL memuat parameter `?tab=` bernilai `history`
24. Verifikasi empty state tab `History` menampilkan judul `No history yet`
25. Verifikasi empty state tab `History` menampilkan deskripsi `Returned and closed borrows and assignments will appear here.`

### Tab Task tersimpan di URL
26. Klik tab `Task`
27. Verifikasi URL memuat parameter `?tab=` bernilai `task`

### Parameter ?tab= yang sah menggantikan tab awal
28. Buka halaman My Asset dengan `?tab=` bernilai `borrowed`
29. Verifikasi tab `Borrowed` terbuka
30. Buka halaman My Asset dengan `?tab=` bernilai `assigned`
31. Verifikasi tab `Assigned` terbuka
32. Buka halaman My Asset dengan `?tab=` bernilai `history`
33. Verifikasi tab `History` terbuka
34. Buka halaman My Asset dengan `?tab=` bernilai `task`
35. Verifikasi tab `Task` terbuka

### Parameter ?tab= tidak valid membuka tab awal Task
36. Buka halaman My Asset dengan `?tab=` bernilai `invoice`
37. Verifikasi tab `Task` terbuka
