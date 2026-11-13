---
id: TC-FA-FAREG-E2E-064-kunci-sesi-take-over
title: "Kunci sesi: Take over dan form pemegang lama"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-19b, FAREG-LOGIC-19f, §4.8#r26, §9.2#p49, §9.2#p51, §9.2#p53, §9.2#p54, §9.2#p55, §9.4.2#r26, §9.6#r12, §9.7#r15, D-REG-22, S-REG-27]
smoke: [D-REG-22, S-REG-27]
dependsOn: []
trace:
  FAREG-LOGIC-19b: [13, 15, 17, 22]
  FAREG-LOGIC-19f: [18, 19]
  §4.8#r26: [13, 15, 17]
  §9.2#p49: 8
  §9.2#p51: 17
  §9.2#p53: 18
  §9.2#p54: [18, 19]
  §9.2#p55: 22
  §9.4.2#r26: [13, 17]
  §9.6#r12: 17
  §9.7#r15: [17, 26]
  D-REG-22: [14, 15]
  S-REG-27: 18
anchor: [3, 25]
coverage:
  web: automated
---

# Kunci sesi: Take over dan form pemegang lama

## Prerequisites
- Aktor:
  - `Rina W` (Manage asset & TAG, Group terkelola `Gudang Kunci {runId}`), pemegang kunci sesi lebih dulu.
  - `Hadi K` (Manage asset & TAG, Group terkelola `Gudang Kunci {runId}`), pengambil alih.
- Layar awal: Rina W dan Hadi K masing-masing di Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - DU-064-1: Draft tersimpan milik `Rina W` untuk Group `Gudang Kunci {runId}`. Item 1 `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `2`; aset 1 ber-Alias Name `Laptop Operasional`.

## Test Steps

### Baseline Registration Log sebelum Take over
1. Hadi K mengetik Search `Gudang Kunci {runId}`, tekan Enter
2. Hadi K mengklik row action `Registration Log` pada baris
3. Verifikasi timeline memuat node `Draft created by Rina W`
4. Hadi K mencatat jumlah node pada timeline
5. Hadi K menekan `Esc` untuk menutup dialog Registration Log

### Aktor kedua membuka batch yang sedang dibuka pemegang kunci
6. Rina W mengetik Search `Gudang Kunci {runId}`, tekan Enter
7. Rina W mengklik Group `Gudang Kunci {runId}` pada baris untuk membuka form Edit
8. Verifikasi form Register Asset batch `Gudang Kunci {runId}` terbuka dalam mode Edit bagi Rina W
9. Rina W mengklik tab `Asset`
10. Rina W mengklik row option `Detail` pada aset 1
11. Rina W mengisi Alias Name `Laptop Rina` pada aset 1 tanpa menyimpan
12. Hadi K mengklik row action `Edit` pada baris batch `Gudang Kunci {runId}`
13. Verifikasi dialog `Draft Is Being Edited` tampil bagi Hadi K
14. Verifikasi isi dialog memuat nama pemegang kunci `Rina W` diikuti kalimat `is editing this draft. If you take over, their unsaved changes will be lost. Do you want to take over?`
15. Verifikasi tombol `[View only]` dan `[Take over]` tampil pada dialog

### Take over memindahkan kunci dan membuat form pemegang lama read-only
16. Hadi K mengklik `[Take over]`
17. Verifikasi form Register Asset batch `Gudang Kunci {runId}` terbuka dalam mode Edit bagi Hadi K
18. Verifikasi form Rina W menampilkan `Alert` Warning `Your edit session was taken over by Hadi K.`
19. Verifikasi form Rina W read-only: tombol `[Save draft]` dan `[Submit]` tidak tampil
20. Hadi K mengklik tab `Asset`
21. Hadi K mengklik row option `Detail` pada aset 1
22. Verifikasi Alias Name aset 1 pada form Hadi K tetap `Laptop Operasional`, sehingga perubahan Rina W `Laptop Rina` yang belum tersimpan tidak ikut tersimpan

### Take over tidak dicatat di Registration Log
23. Hadi K mengklik `[Cancel]` pada form (form belum diubah sejak dibuka)
24. Hadi K mengklik row action `Registration Log` pada baris
25. Verifikasi timeline masih memuat node `Draft created by Rina W`
26. Verifikasi jumlah node sama dengan jumlah yang dicatat sebelum Take over, tanpa node baru
