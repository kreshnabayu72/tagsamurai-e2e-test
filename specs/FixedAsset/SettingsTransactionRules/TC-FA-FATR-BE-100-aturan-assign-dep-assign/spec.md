---
id: TC-FA-FATR-BE-100-aturan-assign-dep-assign
title: "Evaluasi dan penegakan aturan pada transaksi Assign"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r6", "§Aturan Logika Modul#r29", "§Aturan Logika Modul#r105", "§4.1#r114", "§4.1#r115", "§4.1#r116", "§4.1#r117", "§4.1#r118", "§4.1#r119", "§4.1#r120", "§4.1#r134", "§4.1#r174", "§4.1#r184", "§9.2#b92", "§9.2#b426", "§9.2#b427", "§9.2#b428", "§9.2#b433", "§9.2#b434", "§9.2#b437", "§9.2#b384", "§9.2#b392", "§9.2#b405", "§9.2#b406", "§9.2#b407", "§9.2#b408", "§9.2#b409", "§9.2#b410", "§9.2#b423", "§9.2#b429", "§9.2#b430", "§9.2#b431", "§9.4.2#r35", "§9.4.2#r90", "§9.4.2#r130", "§9.4.2#r136", "§9.4.3#b9", "§9.4.4#r54", "§9.7#r6", "§9.7#r15", "§9.8#r4", "§9.8#r5", "§9.10.3#r5", "§9.10.3#b2", "§11#r4", "§4.1#r112", "§4.1#r113", "§4.1#r171", "§4.1#r173", "§9.10.1#r11", "§9.2#b382", "§9.2#b444", "§9.2#b445", "§Aturan Logika Modul#r58"]
smoke: []
dependsOn:
  - "Assign: pengajuan, handover, Reassign, dan Unassign"
owner: BE
trace:
  "§Aturan Logika Modul#r6": [44, 64]
  "§Aturan Logika Modul#r29": 67
  "§Aturan Logika Modul#r105": 96
  "§4.1#r114": 4
  "§4.1#r115": [6, 9]
  "§4.1#r116": [9, 103]
  "§4.1#r117": 53
  "§4.1#r118": [36, 43, 125, 126]
  "§4.1#r119": [42, 110, 112, 113]
  "§4.1#r120": [58, 117, 119]
  "§4.1#r134": [69, 135, 136]
  "§4.1#r174": 2
  "§4.1#r184": [11, 13]
  "§9.2#b92": 64
  "§9.2#b426": [19, 23]
  "§9.2#b427": 21
  "§9.2#b428": 26
  "§9.2#b433": 44
  "§9.2#b434": 45
  "§9.2#b437": 47
  "§9.2#b384": 45
  "§9.2#b392": 77
  "§9.2#b405": [36, 41, 125, 126]
  "§9.2#b406": 39
  "§9.2#b407": 60
  "§9.2#b408": [42, 110, 112, 113]
  "§9.2#b409": [58, 117, 119]
  "§9.2#b410": 44
  "§9.2#b423": [11, 101]
  "§9.2#b429": 28
  "§9.2#b430": [29, 30, 105, 106]
  "§9.2#b431": [16, 131, 133]
  "§9.4.2#r35": [44, 45]
  "§9.4.2#r90": 50
  "§9.4.2#r130": [32, 34]
  "§9.4.2#r136": 47
  "§9.4.3#b9": [86, 87]
  "§9.4.4#r54": 90
  "§9.7#r6": 50
  "§9.7#r15": 64
  "§9.8#r4": [80, 81, 82]
  "§9.8#r5": [83, 84, 85]
  "§9.10.3#r5": 93
  "§9.10.3#b2": 129
  "§11#r4": [60, 80]
  "§4.1#r112": [41, 53]
  "§4.1#r113": 103
  "§4.1#r171": 101
  "§4.1#r173": 11
  "§9.10.1#r11": 90
  "§9.2#b382": 90
  "§9.2#b444": [77, 80]
  "§9.2#b445": 90
  "§Aturan Logika Modul#r58": [32, 34]
---

# Evaluasi dan penegakan aturan pada transaksi Assign

## Prerequisites
- Aktor: Admin `Budi Santoso {runId}` (Total Control entitas khusus; mengubah setting dan mengajukan transaksi Assign); `Tia Anggraini {runId}` (pengaju Assign, bukan Group Manager dan bukan Total Control); `Wawan Hidayat {runId}` (Approver Level 1); Operator platform (hanya mengubah level plan entitas).
- Data:
  - DU-100-1: Entitas: Name `Entitas Aturan Assign {runId}`; entitas khusus spec ini, tidak dipakai spec lain.
  - DU-100-2: Group: Name `Gudang Pusat {runId}`; Group tempat semua aset berada.
  - DU-100-3: User: Name `Budi Santoso {runId}`, Role `Total Control entitas`; Admin pengaju dan pengubah setting.
  - DU-100-4: Employee: Name `Rina Kusuma {runId}`, Status `Aktif`, Akun login `Ada`; Employee assignee di entitas khusus.
  - DU-100-5: Employee: Name `Agus Hartono {runId}`, Status `Aktif`, Akun login `Ada`; Employee assignee di entitas khusus.
  - DU-100-6: Employee: Name `Maya Puspita {runId}`, Status `Aktif`, Akun login `Ada`; Employee assignee di entitas khusus.
  - DU-100-7: Employee: Name `Lina Marlina {runId}`, Status `Aktif`, Akun login `Ada`; Employee assignee di entitas khusus.
  - DU-100-8: Employee: Name `Tono Wibowo {runId}`, Status `Aktif`, Akun login `Ada`; Employee assignee di entitas khusus.
  - DU-100-9: Employee: Name `Hendra Gunawan {runId}`, Status `Aktif`, Akun login `Ada`; Employee assignee di entitas khusus.
  - DU-100-10: Employee: Name `Dedi Pratama {runId}`, Status `Aktif`, Akun login `Tidak ada`; Employee assignee di entitas khusus.
  - DU-100-11: Employee: Name `Sari Wulandari {runId}`, Status `Nonaktif`, Akun login `Ada`; Employee assignee di entitas khusus.
  - DU-100-12: User: Name `Tia Anggraini {runId}`, Role `Pengaju Assign`; Pengaju Assign yang bukan Group Manager dan bukan Total Control.
  - DU-100-13: User: Name `Wawan Hidayat {runId}`, Role Transaksi `Approver`; Approver Level 1 untuk Group di atas.
  - DU-100-14: Category: Name `Laptop {runId}`; Category leaf.
  - DU-100-15: Category: Name `Printer {runId}`; Category leaf.
  - DU-100-16: Category: Name `Monitor {runId}`; Category leaf.
  - DU-100-17: Category: Name `Furnitur Non TAG {runId}`, Penanda `Non TAG`; Category leaf bertanda Non TAG.
  - DU-100-18: Setting Company default Assign: Allow Assign `Allow`, Allowed assignee: Employee `ON`, Allowed assignee: Division `ON`, Max assets per assignee (concurrent) `3`, Need recipient confirmation `Yes`, Photo at start `ON`, Photo at end `ON`, Require approval `OFF`, Transaction timeout `7`; keadaan awal Company default tab Assign.
  - DU-100-19: Asset: Name `Lenovo ThinkPad E14 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`, Status `Assigned`, Pemegang `Rina Kusuma {runId}`; aset berstatus Assigned kepada Rina.
  - DU-100-20: Asset: Name `Dell Latitude 5440 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-21: Asset: Name `HP ProBook 450 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-22: Asset: Name `Asus ExpertBook B1 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-23: Asset: Name `Toshiba Dynabook {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-24: Asset: Name `Acer Aspire 5 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-25: Asset: Name `MacBook Air M2 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-26: Asset: Name `Lenovo ThinkBook 14 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-27: Asset: Name `Dell Vostro 3420 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-28: Asset: Name `Samsung Galaxy Book3 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-29: Asset: Name `Lenovo Legion 5 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`, Tag `Terpasang`; aset ber-tag.
  - DU-100-30: Asset: Name `Asus Vivobook 14 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`, Status `Assigned`, Pemegang `Agus Hartono {runId}`, Tag `Rusak`; aset Assigned kepada Agus dengan tag rusak.
  - DU-100-31: Asset: Name `Toshiba Satellite Pro {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`, Status `Assigned`, Pemegang `Agus Hartono {runId}`; aset berstatus Assigned kepada Agus.
  - DU-100-32: Asset: Name `Microsoft Surface Pro 8 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`, Kondisi `Damaged`; aset berkondisi Damaged.
  - DU-100-33: Asset: Name `Fujitsu Lifebook U7 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`, Kondisi `Missing`; aset berkondisi Missing.
  - DU-100-34: Asset: Name `Printer Epson L3250 {runId}`, Category `Printer {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-35: Asset: Name `Printer Canon G3010 {runId}`, Category `Printer {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-36: Asset: Name `Printer HP LaserJet M111 {runId}`, Category `Printer {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-37: Asset: Name `Printer Brother HL-L2375 {runId}`, Category `Printer {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-38: Asset: Name `Printer Ricoh SP 111 {runId}`, Category `Printer {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-39: Asset: Name `Printer Xerox B230 {runId}`, Category `Printer {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-40: Asset: Name `Printer Kyocera ECOSYS {runId}`, Category `Printer {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-41: Asset: Name `Printer Samsung Xpress M2020 {runId}`, Category `Printer {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-42: Asset: Name `Monitor Dell P2422H {runId}`, Category `Monitor {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-43: Asset: Name `Meja Kerja Staff {runId}`, Category `Furnitur Non TAG {runId}`, Group `Gudang Pusat {runId}`, Tag `Terpasang`; aset ber-tag di Category Non TAG.
  - DU-100-44: Asset: Name `Printer Scanner Fujitsu fi-7160 {runId}`, Category `Printer {runId}`, Group `Gudang Transit {runId}`, Allowed assignee: Employee `OFF`, Allowed assignee: Division `OFF`, Allow Assign `Allow`; aset yang dipindah ke Group Gudang Transit yang ber-override Allowed assignee OFF/OFF, sehingga nilai efektif Allowed assignee OFF/OFF dan Allow Assign bukan Deny.
  - DU-100-57: Employee: Name `Wulan Safitri {runId}`, Status `Aktif`, Akun login `Ada`; Employee assignee di entitas khusus.
  - DU-100-58: Employee: Name `Bagus Prasetyo {runId}`, Status `Aktif`, Akun login `Ada`; Employee assignee di entitas khusus.
  - DU-100-59: Employee: Name `Citra Dewi {runId}`, Status `Aktif`, Akun login `Ada`; Employee assignee di entitas khusus.
  - DU-100-60: Category: Name `Scanner {runId}`; Category leaf.
  - DU-100-61: Category: Name `Proyektor {runId}`; Category leaf.
  - DU-100-62: Category: Name `Kamera {runId}`; Category leaf.
  - DU-100-63: Group: Name `Gudang Cabang Lintas {runId}`; Group dengan override Max assets per assignee All categories.
  - DU-100-64: Group: Name `Gudang Cabang Leaf {runId}`; Group dengan override Max assets per assignee Category leaf.
  - DU-100-65: Group: Name `Gudang Transit {runId}`; Group yang ber-override Allowed assignee OFF/OFF.
  - DU-100-66: Asset: Name `Printer Pantum P2500 {runId}`, Category `Printer {runId}`, Group `Gudang Pusat {runId}`, Tag `Terpasang`; aset di Group Gudang Pusat.
  - DU-100-67: Asset: Name `Asus Zenbook 14 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`, Status `Assigned`, Pemegang `Agus Hartono {runId}`, Tag `Rusak`; aset di Group Gudang Pusat.
  - DU-100-68: Asset: Name `Printer Lexmark MS431 {runId}`, Category `Printer {runId}`, Group `Gudang Pusat {runId}`; aset di Group Gudang Pusat.
  - DU-100-69: Asset: Name `Scanner Epson DS-530 {runId}`, Category `Scanner {runId}`, Group `Gudang Cabang Lintas {runId}`; aset di Group Gudang Cabang Lintas.
  - DU-100-70: Asset: Name `Proyektor Epson EB-X06 {runId}`, Category `Proyektor {runId}`, Group `Gudang Cabang Lintas {runId}`; aset di Group Gudang Cabang Lintas.
  - DU-100-71: Asset: Name `Kamera Canon EOS 200D {runId}`, Category `Kamera {runId}`, Group `Gudang Cabang Lintas {runId}`; aset di Group Gudang Cabang Lintas.
  - DU-100-72: Asset: Name `Proyektor BenQ MX560 {runId}`, Category `Proyektor {runId}`, Group `Gudang Cabang Leaf {runId}`; aset di Group Gudang Cabang Leaf.
  - DU-100-73: Asset: Name `Kamera Nikon D3500 {runId}`, Category `Kamera {runId}`, Group `Gudang Cabang Leaf {runId}`; aset di Group Gudang Cabang Leaf.
  - DU-100-74: Asset: Name `Kamera Sony ZV-E10 {runId}`, Category `Kamera {runId}`, Group `Gudang Cabang Leaf {runId}`; aset di Group Gudang Cabang Leaf.
  - DU-100-79: Employee: Name `Galih Permana {runId}`, Status `Aktif`, Akun login `Ada`; Employee pemegang aset untuk Unassign serah terima fisik.
  - DU-100-80: Asset: Name `Lenovo IdeaPad Slim 3 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`, Status `Assigned`, Pemegang `Galih Permana {runId}`; aset Assigned kepada Galih untuk Unassign dengan foto.
  - DU-100-81: Asset: Name `Acer Swift 3 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`, Status `Assigned`, Pemegang `Galih Permana {runId}`, Tag `Rusak`; aset Assigned kepada Galih dengan tag rusak untuk Unassign lewat `I can't scan the TAG`.
  - Spec ini memakai entitas khusus (DU-100-1) yang tidak dipakai spec lain; semua data di atas berada di entitas itu.
- Kondisi:
  - Company default tab Assign pada keadaan awal sesuai DU-100-18: Allow Assign bernilai `Allow`, Allowed assignee: Employee bernilai `ON`, Allowed assignee: Division bernilai `ON`, Max assets per assignee (concurrent) bernilai `3`, Need recipient confirmation bernilai `Yes`, Photo at start bernilai `ON`, Photo at end bernilai `ON`, Require approval bernilai `OFF`, Transaction timeout bernilai `7` hari
  - Level Feature Suite Assignment pada plan entitas bernilai `Full` dan Approval Workflow tersedia
  - Category leaf `Laptop {runId}`, `Printer {runId}`, dan `Monitor {runId}` mewarisi Company default (Inherit) pada semua field
  - Employee `Agus Hartono {runId}` memegang aset berstatus Assigned sesuai DU di atas
  - `Wawan Hidayat {runId}` adalah satu-satunya Approver Level 1 untuk Group `Gudang Pusat {runId}`
  - Group `Gudang Transit {runId}` ber-override Allowed assignee: Employee `OFF` dan Allowed assignee: Division `OFF` pada transaksi Assign, dan aset `Printer Scanner Fujitsu fi-7160 {runId}` dipindahkan ke Group itu lewat operasi di luar halaman Settings, sehingga kombinasi efektif OFF/OFF lolos dari validasi halaman

## Test Steps
### Pengajuan Assign tanpa approval dimulai dari Handover
1. Admin `Budi Santoso {runId}` mengajukan Assign aset `Dell Latitude 5440 {runId}` kepada `Lina Marlina {runId}`
2. Verifikasi pengajuan diterima dan baris Assign berstatus `Waiting for Handover`, yaitu Handover adalah langkah awal Assign

### Assignee Employee harus aktif dan punya akun login
3. Admin mengajukan Assign aset `MacBook Air M2 {runId}` kepada `Sari Wulandari {runId}`
4. Verifikasi pengajuan ditolak karena assignee Employee harus aktif, dan tidak ada baris Assign baru untuk aset `MacBook Air M2 {runId}`
5. Admin mengajukan Assign aset `MacBook Air M2 {runId}` kepada `Dedi Pratama {runId}` pada Need recipient confirmation `Yes`
6. Verifikasi pengajuan ditolak karena assignee Employee harus punya akun login pada Need recipient confirmation `Yes`
7. Admin menyimpan Company default Assign dengan Need recipient confirmation `No`
8. Admin mengajukan Assign aset `MacBook Air M2 {runId}` kepada `Dedi Pratama {runId}`
9. Verifikasi pengajuan tetap ditolak karena akun login tetap wajib pada Need recipient confirmation `No`, yang hanya menghilangkan langkah akseptasi saat handover

### Photo at end wajib pada Unassign
10. Admin menyelesaikan Unassign aset `Toshiba Satellite Pro {runId}` dari `Agus Hartono {runId}` tanpa foto
11. Verifikasi Unassign ditolak karena Photo at end `ON` mewajibkan 1 foto pada akhir transaksi Assign
12. Admin menyelesaikan Unassign aset `Toshiba Satellite Pro {runId}` dari `Agus Hartono {runId}` dengan satu foto
13. Verifikasi Unassign diterima dan aset `Toshiba Satellite Pro {runId}` tidak lagi dipegang `Agus Hartono {runId}`

### Handover Note PDF dibuat untuk serah terima fisik
14. Admin mengajukan Assign aset `Dell Vostro 3420 {runId}` kepada `Lina Marlina {runId}`
15. Admin menjalankan langkah mulai Handover aset `Dell Vostro 3420 {runId}` dengan satu foto
16. Verifikasi Handover Note PDF dibuat untuk serah terima aset `Dell Vostro 3420 {runId}`

### Scan tag wajib saat mulai transaksi aset ber-tag
17. Admin mengajukan Assign aset ber-tag `Lenovo Legion 5 {runId}` kepada `Lina Marlina {runId}`
18. Admin menjalankan langkah mulai Handover aset `Lenovo Legion 5 {runId}` dengan satu foto tanpa scan tag
19. Verifikasi langkah mulai ditolak karena scan tag wajib saat mulai transaksi untuk aset ber-tag
20. Admin menjalankan langkah mulai Handover aset `Lenovo Legion 5 {runId}` dengan satu foto lewat identifikasi manual tanpa scan tag
21. Verifikasi langkah mulai ditolak karena tidak ada identifikasi manual untuk langkah mulai
22. Admin menjalankan langkah mulai Handover aset `Lenovo Legion 5 {runId}` dengan satu foto dan scan tag aset itu
23. Verifikasi langkah mulai diterima dan aset `Lenovo Legion 5 {runId}` berstatus `Assigned` kepada `Lina Marlina {runId}`

### Category Non TAG dikecualikan dari scan tag wajib
24. Admin mengajukan Assign aset `Meja Kerja Staff {runId}` kepada `Agus Hartono {runId}`
25. Admin menjalankan langkah mulai Handover aset `Meja Kerja Staff {runId}` dengan satu foto tanpa scan tag
26. Verifikasi langkah mulai diterima tanpa scan tag karena Category `Furnitur Non TAG {runId}` bertanda Non TAG

### Unassign lewat I can't scan the TAG saat tag rusak
27. Admin menyelesaikan Unassign aset `Asus Vivobook 14 {runId}` dari `Agus Hartono {runId}` lewat `I can't scan the TAG` dengan satu foto
28. Verifikasi Unassign diterima walau tag rusak
29. Verifikasi flag `Manual identification` tercatat pada transaksi Unassign aset `Asus Vivobook 14 {runId}`
30. Verifikasi Report TAG untuk aset `Asus Vivobook 14 {runId}` dibuat otomatis

### Aset Damaged atau Missing tidak dapat di-Assign
31. Admin mengajukan Assign aset `Microsoft Surface Pro 8 {runId}` kepada `Tono Wibowo {runId}`
32. Verifikasi pengajuan ditolak karena aset dengan kondisi rusak tidak dapat di-Assign
33. Admin mengajukan Assign aset `Fujitsu Lifebook U7 {runId}` kepada `Tono Wibowo {runId}`
34. Verifikasi pengajuan ditolak karena aset dengan kondisi hilang tidak dapat di-Assign

### Kuota Max assets per assignee di bawah batas
35. Admin mengajukan Assign aset `Printer Epson L3250 {runId}` kepada `Rina Kusuma {runId}`, yang memegang `Lenovo ThinkPad E14 {runId}` berstatus `Assigned`, pada Max assets per assignee (concurrent) `3`
36. Verifikasi pengajuan diterima pada total `2` baris aktif Rina termasuk baris baru, satu di bawah batas `3`, dengan baris `Assigned` ikut dihitung

### Draft tidak dihitung dan kuota tepat di batas
37. Admin menyimpan Draft Assign aset `HP ProBook 450 {runId}` untuk `Rina Kusuma {runId}`
38. Admin mengajukan Assign aset `Lenovo ThinkBook 14 {runId}` kepada `Rina Kusuma {runId}`
39. Verifikasi pengajuan diterima pada total tepat `3` baris aktif Rina, dan Draft `HP ProBook 450 {runId}` tidak ikut dihitung

### Kuota di atas batas ditolak di server
40. Admin mengirim pengajuan Assign aset `Asus ExpertBook B1 {runId}` kepada `Rina Kusuma {runId}` langsung ke server tanpa melalui tampilan
41. Verifikasi pengajuan ditolak karena total `4` baris aktif Rina melebihi batas `3`
42. Verifikasi kuota dihitung lintas Category karena baris aktif Rina di Category `Laptop {runId}` saja berjumlah `2` dan baru terlampaui bersama baris di Category `Printer {runId}`, pada nilai `3` dari Company default
43. Verifikasi tidak ada baris Assign baru untuk aset `Asus ExpertBook B1 {runId}` dan jumlah baris aktif Rina tetap `3`
44. Verifikasi penolakan berlaku untuk permintaan yang dikirim langsung ke server, apa pun keadaan tampilan
45. Verifikasi pesan blokir menyebut siapa yang dapat dihubungi

### Perubahan Max assets per assignee berlaku untuk transaksi baru
46. Admin menyimpan Company default Assign dengan Max assets per assignee (concurrent) `2`
47. Verifikasi tiga baris aktif Rina tidak dibatalkan otomatis dan tetap pada status semula: `Lenovo ThinkPad E14 {runId}` `Assigned`, `Printer Epson L3250 {runId}` `Waiting for Handover`, `Lenovo ThinkBook 14 {runId}` `Waiting for Handover`
48. Admin menyimpan Company default Assign dengan Max assets per assignee (concurrent) `4`
49. Admin mengajukan Assign aset `Asus ExpertBook B1 {runId}` kepada `Rina Kusuma {runId}`
50. Verifikasi pengajuan diterima pada total `4` baris aktif Rina, yang pada batas `3` ditolak, sehingga nilai baru berlaku untuk transaksi baru

### Nilai 0 berarti Unlimited
51. Admin menyimpan Company default Assign dengan Max assets per assignee (concurrent) `0`
52. Admin mengajukan Assign aset `Toshiba Dynabook {runId}` kepada `Rina Kusuma {runId}`
53. Verifikasi pengajuan diterima walau Rina sudah memiliki `4` baris aktif, karena `0` berarti Unlimited

### Kuota dihitung per Category dari nilai efektif aset yang diajukan
54. Admin menyimpan Company default Assign dengan Max assets per assignee (concurrent) `3`
55. Admin menyimpan Category leaf `Laptop {runId}` dengan Max assets per assignee (concurrent) `1` sebagai nilai sendiri
56. Admin mengajukan Assign aset `Printer Canon G3010 {runId}` kepada `Maya Puspita {runId}`
57. Admin mengajukan Assign aset `Acer Aspire 5 {runId}` kepada `Maya Puspita {runId}`
58. Verifikasi pengajuan diterima karena kuota dihitung di Category `Laptop {runId}` saja: baris aktif Maya di Category itu `1` setelah baris baru, walau total lintas Category `2`
59. Admin mengajukan Assign aset `MacBook Air M2 {runId}` kepada `Maya Puspita {runId}`
60. Verifikasi pengajuan ditolak karena nilai kuota yang dipakai adalah nilai efektif aset yang diajukan, yaitu `1` dari Category leaf `Laptop {runId}` dan bukan `3` dari Company default: baris aktif Maya di Category itu menjadi `2`, sedangkan total lintas Category `3` masih di dalam batas `3`

### Deny pada override mengalahkan nilai lain dan Deny Category dievaluasi di server
61. Admin membuat override pada Group `Gudang Pusat {runId}` untuk transaksi Assign dengan Allow Assign `Allow`
62. Admin membuat override pada aset `Samsung Galaxy Book3 {runId}` untuk transaksi Assign dengan Allow Assign `Deny`
63. Admin mengajukan Assign aset `Samsung Galaxy Book3 {runId}` kepada `Tono Wibowo {runId}`
64. Verifikasi pengajuan ditolak walau override Group bernilai `Allow`, karena Deny pada override aset mengalahkan semua nilai lain
65. Admin menyimpan Category leaf `Monitor {runId}` dengan Allow Assign `Deny`
66. Admin mengirim pengajuan Assign aset `Monitor Dell P2422H {runId}` kepada `Tono Wibowo {runId}` langsung ke server tanpa melalui tampilan
67. Verifikasi pengajuan ditolak karena Deny pada Category tetap dievaluasi ulang di server

### Kombinasi efektif Allowed assignee OFF/OFF ditolak
68. Admin mengajukan Assign aset `Printer Scanner Fujitsu fi-7160 {runId}` kepada `Tono Wibowo {runId}`
69. Verifikasi pengajuan ditolak karena tidak ada tipe Assignee yang diizinkan: nilai efektif Allowed assignee: Employee `OFF` dan Allowed assignee: Division `OFF`, sedangkan nilai efektif Allow Assign bukan `Deny`

### Transaction timeout menutup transaksi Assign yang menunggu
70. Admin menyimpan Company default Assign dengan Require approval `ON`
71. Admin menyimpan Company default Assign dengan Transaction timeout `1`
72. `Tia Anggraini {runId}` mengajukan Assign aset `Printer Brother HL-L2375 {runId}` kepada `Tono Wibowo {runId}`, sehingga berstatus `Waiting for Approval`
73. `Tia Anggraini {runId}` mengajukan Assign aset `Printer Ricoh SP 111 {runId}` kepada `Tono Wibowo {runId}`
74. `Wawan Hidayat {runId}` menyetujui pengajuan Assign aset `Printer Ricoh SP 111 {runId}`, sehingga berstatus `Waiting for Handover`
75. Waktu berlalu 23 jam sejak kedua transaksi masuk statusnya
76. Background job pengecekan Transaction timeout berjalan
77. Verifikasi baris Assign aset `Printer Brother HL-L2375 {runId}` masih `Waiting for Approval` dan baris Assign aset `Printer Ricoh SP 111 {runId}` masih `Waiting for Handover`, karena batas Transaction timeout `1` hari sejak transaksi masuk status menunggu belum tercapai
78. Waktu berlalu sampai 1 hari sejak kedua transaksi masuk statusnya
79. Background job pengecekan Transaction timeout berjalan
80. Verifikasi baris Assign aset `Printer Brother HL-L2375 {runId}` berstatus `Canceled`
81. Verifikasi Note baris itu `Timed out (Waiting for Approval)`
82. Verifikasi log transaksi baris itu tercatat dengan Modified By `System`
83. Verifikasi baris Assign aset `Printer Ricoh SP 111 {runId}` berstatus `Canceled`
84. Verifikasi Note baris itu `Not handed over`
85. Verifikasi log transaksi baris itu tercatat dengan Modified By `System`
86. Verifikasi Draft Assign aset `HP ProBook 450 {runId}` tetap Draft dan tidak ditutup otomatis
87. Verifikasi baris Assign aset `Lenovo ThinkPad E14 {runId}` tetap berstatus `Assigned` dan tidak ditutup otomatis

### Approval dilewati saat Approval Workflow tidak tersedia di plan
88. Operator platform mengubah Approval Workflow pada plan entitas menjadi tidak tersedia, dengan Require approval tersimpan `ON`
89. `Tia Anggraini {runId}` mengajukan Assign aset `Printer Xerox B230 {runId}` kepada `Tono Wibowo {runId}`
90. Verifikasi pengajuan tidak berstatus `Waiting for Approval` melainkan `Waiting for Handover`, karena nilai efektif Require approval `OFF` untuk transaksi Assign

### Level Feature Suite Assignment Basic menerima Assign kepada Employee
91. Operator platform mengubah level Feature Suite Assignment pada plan entitas menjadi `Basic`
92. Admin mengajukan Assign aset `Printer Kyocera ECOSYS {runId}` kepada `Tono Wibowo {runId}`
93. Verifikasi pengajuan Assign kepada Employee diterima pada level `Basic`, karena tipe assignee Employee selalu tersedia pada level itu; tipe assignee Division tidak tersedia pada level `Basic` (Allowed assignee: Division terkunci, nilai efektif `OFF`)

### Level Feature Suite Assignment None membuat Assign tidak tersedia
94. Operator platform mengubah level Feature Suite Assignment pada plan entitas menjadi `None`
95. Admin mengajukan Assign aset `Printer Samsung Xpress M2020 {runId}` kepada `Hendra Gunawan {runId}`
96. Verifikasi pengajuan ditolak karena pada level `None` Assign tidak tersedia

### Photo at start wajib pada Handover Assign dan Optional tanpa akseptasi
97. Operator platform mengubah level Feature Suite Assignment pada plan entitas menjadi `Full`
98. Admin menyimpan Company default Assign dengan Require approval `OFF`
99. Admin mengajukan Assign aset ber-tag `Printer Pantum P2500 {runId}` kepada `Hendra Gunawan {runId}`
100. Admin menjalankan langkah mulai Handover aset `Printer Pantum P2500 {runId}` dengan scan tag aset itu tanpa foto
101. Verifikasi langkah mulai ditolak karena Photo at start `ON` mewajibkan 1 foto pada langkah awal transaksi Assign, dan baris tetap berstatus `Waiting for Handover`
102. Admin menjalankan langkah mulai Handover aset `Printer Pantum P2500 {runId}` dengan satu foto dan scan tag aset itu
103. Verifikasi Handover selesai dan aset `Printer Pantum P2500 {runId}` berstatus `Assigned` kepada `Hendra Gunawan {runId}` tanpa akseptasi dari Assignee, karena Need recipient confirmation `No` hanya menghilangkan langkah akseptasi saat handover

### Foto tanpa cek radius pada Unassign lewat I can't scan the TAG
104. Admin menyelesaikan Unassign aset `Asus Zenbook 14 {runId}` dari `Agus Hartono {runId}` lewat `I can't scan the TAG` dengan satu foto
105. Verifikasi foto yang disertakan tercatat pada transaksi Unassign aset `Asus Zenbook 14 {runId}`
106. Verifikasi Unassign aset `Asus Zenbook 14 {runId}` lewat `I can't scan the TAG` diterima dengan identifikasi manual berupa foto aset, tanpa cek radius

### Kuota dari override All categories dihitung lintas Category
107. Admin membuat override pada Group `Gudang Cabang Lintas {runId}` di All categories untuk transaksi Assign dengan Max assets per assignee (concurrent) `2`
108. Admin mengajukan Assign aset `Scanner Epson DS-530 {runId}` kepada `Bagus Prasetyo {runId}`
109. Admin mengajukan Assign aset `Proyektor Epson EB-X06 {runId}` kepada `Bagus Prasetyo {runId}`
110. Verifikasi kedua pengajuan diterima pada total `2` baris aktif Bagus, tepat di batas `2` dari override All categories
111. Admin mengajukan Assign aset `Kamera Canon EOS 200D {runId}` kepada `Bagus Prasetyo {runId}`
112. Verifikasi pengajuan ditolak karena nilai `2` bersumber dari override ber-Category All categories sehingga kuota dihitung lintas Category: total `3` baris aktif Bagus melebihi `2`, walau baris aktif di Category `Kamera {runId}` saja hanya `1`
113. Verifikasi tidak ada baris Assign baru untuk aset `Kamera Canon EOS 200D {runId}` dan jumlah baris aktif Bagus tetap `2`

### Kuota dari override Category leaf dihitung di Category itu
114. Admin membuat override pada Group `Gudang Cabang Leaf {runId}` di Category `Kamera {runId}` untuk transaksi Assign dengan Max assets per assignee (concurrent) `1`
115. Admin mengajukan Assign aset `Proyektor BenQ MX560 {runId}` kepada `Citra Dewi {runId}`
116. Admin mengajukan Assign aset `Kamera Nikon D3500 {runId}` kepada `Citra Dewi {runId}`
117. Verifikasi pengajuan aset `Kamera Nikon D3500 {runId}` diterima karena nilai `1` bersumber dari override ber-Category leaf `Kamera {runId}` sehingga kuota dihitung di Category itu saja: baris aktif Citra di Category itu `1` setelah baris baru, walau total lintas Category `2`
118. Admin mengajukan Assign aset `Kamera Sony ZV-E10 {runId}` kepada `Citra Dewi {runId}`
119. Verifikasi pengajuan aset `Kamera Sony ZV-E10 {runId}` ditolak karena baris aktif Citra di Category `Kamera {runId}` menjadi `2`, melebihi nilai `1` dari override ber-Category leaf

### Baris Waiting for Approval ikut dihitung sebagai baris aktif
120. Operator platform mengubah Approval Workflow pada plan entitas menjadi tersedia
121. Admin menyimpan Company default Assign dengan Require approval `ON`
122. Admin menyimpan Company default Assign dengan Max assets per assignee (concurrent) `1`
123. `Tia Anggraini {runId}` mengajukan Assign aset `Printer HP LaserJet M111 {runId}` kepada `Wulan Safitri {runId}`, sehingga berstatus `Waiting for Approval`
124. `Tia Anggraini {runId}` mengajukan Assign aset `Printer Lexmark MS431 {runId}` kepada `Wulan Safitri {runId}`
125. Verifikasi pengajuan aset `Printer Lexmark MS431 {runId}` ditolak karena baris `Waiting for Approval` milik `Wulan Safitri {runId}` ikut dihitung sebagai baris aktif: total `2` baris aktif melebihi batas `1`
126. Verifikasi tidak ada baris Assign baru untuk aset `Printer Lexmark MS431 {runId}` dan baris aset `Printer HP LaserJet M111 {runId}` tetap `Waiting for Approval`

### Perubahan level plan bukan perubahan Settings dan tidak masuk Changelog
127. Admin mencatat entri teratas Changelog Transaction Settings
128. Operator platform mengubah level Feature Suite Assignment pada plan entitas menjadi `Basic`
129. Verifikasi entri teratas Changelog Transaction Settings tetap sama dan tidak ada entri baru dalam 5 detik, karena perubahan level plan bukan perubahan Settings

### Handover Note PDF dibuat pada serah terima fisik Unassign
130. Admin menyelesaikan Unassign aset `Lenovo IdeaPad Slim 3 {runId}` dari `Galih Permana {runId}` dengan satu foto
131. Verifikasi Handover Note PDF dibuat untuk serah terima aset `Lenovo IdeaPad Slim 3 {runId}` pada Unassign
132. Admin menyelesaikan Unassign aset `Acer Swift 3 {runId}` dari `Galih Permana {runId}` lewat `I can't scan the TAG` dengan satu foto
133. Verifikasi Handover Note PDF dibuat untuk serah terima aset `Acer Swift 3 {runId}` pada Unassign lewat `I can't scan the TAG`

### Pesan blokir kombinasi Allowed assignee OFF/OFF menyebut siapa yang dapat dihubungi
134. Admin mengajukan Assign aset `Printer Scanner Fujitsu fi-7160 {runId}` kepada `Tono Wibowo {runId}`
135. Verifikasi pengajuan ditolak
136. Verifikasi pesan blokir penolakan itu menyebut siapa yang dapat dihubungi
