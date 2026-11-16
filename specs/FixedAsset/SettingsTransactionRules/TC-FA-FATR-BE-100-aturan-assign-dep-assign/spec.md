---
id: TC-FA-FATR-BE-100-aturan-assign-dep-assign
title: "Evaluasi dan penegakan aturan pada transaksi Assign"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r6", "§Aturan Logika Modul#r26", "§Aturan Logika Modul#r109", "§4.1#r104", "§4.1#r105", "§4.1#r106", "§4.1#r107", "§4.1#r108", "§4.1#r109", "§4.1#r110", "§4.1#r124", "§4.1#r164", "§4.1#r167", "§4.1#r168", "§4.1#r176", "§9.2#b92", "§9.2#b427", "§9.2#b428", "§9.2#b429", "§9.2#b434", "§9.2#b435", "§9.2#b438", "§9.2#b384", "§9.2#b392", "§9.2#b405", "§9.2#b406", "§9.2#b407", "§9.2#b408", "§9.2#b409", "§9.2#b410", "§9.2#b412", "§9.2#b424", "§9.2#b430", "§9.2#b431", "§9.2#b432", "§9.4.2#r35", "§9.4.2#r82", "§9.4.2#r122", "§9.4.2#r128", "§9.4.3#b9", "§9.4.4#r54", "§9.7#r6", "§9.7#r15", "§9.8#r4", "§9.8#r5", "§9.10.3#r5", "§9.10.3#b2", "§9.10.3#b7", "§11#r4"]
smoke: []
dependsOn:
  - "Assign: pengajuan, handover, Reassign, dan Unassign"
owner: BE
trace:
  "§Aturan Logika Modul#r6": [46, 66]
  "§Aturan Logika Modul#r26": 69
  "§Aturan Logika Modul#r109": 103
  "§4.1#r104": 4
  "§4.1#r105": [6, 9]
  "§4.1#r106": [9, 110]
  "§4.1#r107": 55
  "§4.1#r108": [38, 45, 132, 133]
  "§4.1#r109": [44, 117, 119, 120]
  "§4.1#r110": [60, 124, 126]
  "§4.1#r124": 71
  "§4.1#r164": 2
  "§4.1#r167": 16
  "§4.1#r168": 17
  "§4.1#r176": [11, 13]
  "§9.2#b92": 66
  "§9.2#b427": [21, 25]
  "§9.2#b428": 23
  "§9.2#b429": 28
  "§9.2#b434": 46
  "§9.2#b435": 47
  "§9.2#b438": 49
  "§9.2#b384": 47
  "§9.2#b392": 79
  "§9.2#b405": [38, 132, 133]
  "§9.2#b406": 41
  "§9.2#b407": 62
  "§9.2#b408": [44, 117, 119, 120]
  "§9.2#b409": [60, 124, 126]
  "§9.2#b410": 46
  "§9.2#b412": 43
  "§9.2#b424": [11, 108]
  "§9.2#b430": 30
  "§9.2#b431": [31, 32, 112, 113]
  "§9.2#b432": 18
  "§9.4.2#r35": [46, 47]
  "§9.4.2#r82": 52
  "§9.4.2#r122": [34, 36]
  "§9.4.2#r128": 49
  "§9.4.3#b9": [88, 89]
  "§9.4.4#r54": 92
  "§9.7#r6": 52
  "§9.7#r15": 66
  "§9.8#r4": [82, 83, 84]
  "§9.8#r5": [85, 86, 87]
  "§9.10.3#r5": 95
  "§9.10.3#b2": 97
  "§9.10.3#b7": 100
  "§11#r4": [62, 82]
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
  - DU-100-18: Setting Company default Assign: Allow Assign `Allow`, Allowed assignee: Employee `ON`, Allowed assignee: Division `ON`, Max assets per assignee (concurrent) `3`, Recipient acceptance `Required`, Direct handover between holders `Allow`, Photo at start `ON`, Photo at end `ON`, Require approval `OFF`, Transaction timeout `7`; keadaan awal Company default tab Assign.
  - DU-100-19: Asset: Name `Lenovo ThinkPad E14 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`, Status `Assigned`, Pemegang `Rina Kusuma {runId}`; aset berstatus Assigned kepada Rina.
  - DU-100-20: Asset: Name `Dell Latitude 5440 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-21: Asset: Name `HP ProBook 450 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-22: Asset: Name `Asus ExpertBook B1 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-23: Asset: Name `Toshiba Dynabook {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-24: Asset: Name `Acer Aspire 5 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-25: Asset: Name `MacBook Air M2 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`; aset di Group `Gudang Pusat {runId}`.
  - DU-100-26: Asset: Name `Lenovo ThinkBook 14 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`, Status `Assigned`, Pemegang `Agus Hartono {runId}`; aset berstatus Assigned kepada Agus.
  - DU-100-27: Asset: Name `Dell Vostro 3420 {runId}`, Category `Laptop {runId}`, Group `Gudang Pusat {runId}`, Status `Assigned`, Pemegang `Agus Hartono {runId}`; aset berstatus Assigned kepada Agus.
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
  - Spec ini memakai entitas khusus (DU-100-1) yang tidak dipakai spec lain; semua data di atas berada di entitas itu.
- Kondisi:
  - Company default tab Assign pada keadaan awal sesuai DU-100-18: Allow Assign bernilai `Allow`, Allowed assignee: Employee bernilai `ON`, Allowed assignee: Division bernilai `ON`, Max assets per assignee (concurrent) bernilai `3`, Recipient acceptance bernilai `Required`, Direct handover between holders bernilai `Allow`, Photo at start bernilai `ON`, Photo at end bernilai `ON`, Require approval bernilai `OFF`, Transaction timeout bernilai `7` hari
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
5. Admin mengajukan Assign aset `MacBook Air M2 {runId}` kepada `Dedi Pratama {runId}` pada Recipient acceptance `Required`
6. Verifikasi pengajuan ditolak karena assignee Employee harus punya akun login pada Recipient acceptance `Required`
7. Admin menyimpan Company default Assign dengan Recipient acceptance `Optional`
8. Admin mengajukan Assign aset `MacBook Air M2 {runId}` kepada `Dedi Pratama {runId}`
9. Verifikasi pengajuan tetap ditolak karena akun login tetap wajib pada Recipient acceptance `Optional`, yang hanya menghilangkan langkah akseptasi saat handover

### Photo at end wajib pada Unassign
10. Admin menyelesaikan Unassign aset `Toshiba Satellite Pro {runId}` dari `Agus Hartono {runId}` tanpa foto
11. Verifikasi Unassign ditolak karena Photo at end `ON` mewajibkan 1 foto pada akhir transaksi Assign
12. Admin menyelesaikan Unassign aset `Toshiba Satellite Pro {runId}` dari `Agus Hartono {runId}` dengan satu foto
13. Verifikasi Unassign diterima dan aset `Toshiba Satellite Pro {runId}` tidak lagi dipegang `Agus Hartono {runId}`

### Satu foto handover memenuhi Reassign
14. Admin mengajukan Reassign aset `Dell Vostro 3420 {runId}` dari `Agus Hartono {runId}` kepada `Lina Marlina {runId}` melalui Direct handover between holders
15. Admin menyelesaikan Handover Reassign aset `Dell Vostro 3420 {runId}` dengan satu foto handover
16. Verifikasi serah terima selesai dan satu foto handover itu memenuhi Photo at end `Agus Hartono {runId}` sebagai pemegang lama
17. Verifikasi serah terima yang sama memenuhi Photo at start `Lina Marlina {runId}` sebagai pemegang baru
18. Verifikasi Handover Note PDF dibuat untuk serah terima aset `Dell Vostro 3420 {runId}`

### Scan tag wajib saat mulai transaksi aset ber-tag
19. Admin mengajukan Assign aset ber-tag `Lenovo Legion 5 {runId}` kepada `Lina Marlina {runId}`
20. Admin menjalankan langkah mulai Handover aset `Lenovo Legion 5 {runId}` dengan satu foto tanpa scan tag
21. Verifikasi langkah mulai ditolak karena scan tag wajib saat mulai transaksi untuk aset ber-tag
22. Admin menjalankan langkah mulai Handover aset `Lenovo Legion 5 {runId}` dengan satu foto lewat identifikasi manual tanpa scan tag
23. Verifikasi langkah mulai ditolak karena tidak ada identifikasi manual untuk langkah mulai
24. Admin menjalankan langkah mulai Handover aset `Lenovo Legion 5 {runId}` dengan satu foto dan scan tag aset itu
25. Verifikasi langkah mulai diterima dan aset `Lenovo Legion 5 {runId}` berstatus `Assigned` kepada `Lina Marlina {runId}`

### Category Non TAG dikecualikan dari scan tag wajib
26. Admin mengajukan Assign aset `Meja Kerja Staff {runId}` kepada `Agus Hartono {runId}`
27. Admin menjalankan langkah mulai Handover aset `Meja Kerja Staff {runId}` dengan satu foto tanpa scan tag
28. Verifikasi langkah mulai diterima tanpa scan tag karena Category `Furnitur Non TAG {runId}` bertanda Non TAG

### Unassign lewat I can't scan the TAG saat tag rusak
29. Admin menyelesaikan Unassign aset `Asus Vivobook 14 {runId}` dari `Agus Hartono {runId}` lewat `I can't scan the TAG` dengan satu foto dari lokasi di dalam radius aset
30. Verifikasi Unassign diterima walau tag rusak
31. Verifikasi flag tercatat pada transaksi Unassign aset `Asus Vivobook 14 {runId}`
32. Verifikasi Report TAG untuk aset `Asus Vivobook 14 {runId}` dibuat otomatis

### Aset Damaged atau Missing tidak dapat di-Assign
33. Admin mengajukan Assign aset `Microsoft Surface Pro 8 {runId}` kepada `Tono Wibowo {runId}`
34. Verifikasi pengajuan ditolak karena aset dengan kondisi rusak tidak dapat di-Assign
35. Admin mengajukan Assign aset `Fujitsu Lifebook U7 {runId}` kepada `Tono Wibowo {runId}`
36. Verifikasi pengajuan ditolak karena aset dengan kondisi hilang tidak dapat di-Assign

### Kuota Max assets per assignee di bawah batas
37. Admin mengajukan Assign aset `Printer Epson L3250 {runId}` kepada `Rina Kusuma {runId}`, yang memegang `Lenovo ThinkPad E14 {runId}` berstatus `Assigned`, pada Max assets per assignee (concurrent) `3`
38. Verifikasi pengajuan diterima pada total `2` baris aktif Rina termasuk baris baru, satu di bawah batas `3`, dengan baris `Assigned` ikut dihitung

### Draft tidak dihitung dan kuota tepat di batas
39. Admin menyimpan Draft Assign aset `HP ProBook 450 {runId}` untuk `Rina Kusuma {runId}`
40. Admin mengajukan Reassign aset `Lenovo ThinkBook 14 {runId}` dari `Agus Hartono {runId}` kepada `Rina Kusuma {runId}` melalui Direct handover between holders
41. Verifikasi pengajuan diterima pada total tepat `3` baris aktif Rina, dan Draft `HP ProBook 450 {runId}` tidak ikut dihitung

### Kuota di atas batas ditolak di server
42. Admin mengirim pengajuan Assign aset `Asus ExpertBook B1 {runId}` kepada `Rina Kusuma {runId}` langsung ke server tanpa melalui tampilan
43. Verifikasi pengajuan ditolak karena total `4` baris aktif Rina, termasuk baris Reassign yang dihitung untuk Rina sejak Submit, melebihi batas `3`
44. Verifikasi kuota dihitung lintas Category karena baris aktif Rina di Category `Laptop {runId}` saja berjumlah `2` dan baru terlampaui bersama baris di Category `Printer {runId}`, pada nilai `3` dari Company default
45. Verifikasi tidak ada baris Assign baru untuk aset `Asus ExpertBook B1 {runId}` dan jumlah baris aktif Rina tetap `3`
46. Verifikasi penolakan berlaku untuk permintaan yang dikirim langsung ke server, apa pun keadaan tampilan
47. Verifikasi pesan blokir menyebut siapa yang dapat dihubungi

### Perubahan Max assets per assignee berlaku untuk transaksi baru
48. Admin menyimpan Company default Assign dengan Max assets per assignee (concurrent) `2`
49. Verifikasi tiga baris aktif Rina tidak dibatalkan otomatis dan tetap pada status semula: `Lenovo ThinkPad E14 {runId}` `Assigned`, `Printer Epson L3250 {runId}` `Waiting for Handover`, `Lenovo ThinkBook 14 {runId}` `Waiting for Handover`
50. Admin menyimpan Company default Assign dengan Max assets per assignee (concurrent) `4`
51. Admin mengajukan Assign aset `Asus ExpertBook B1 {runId}` kepada `Rina Kusuma {runId}`
52. Verifikasi pengajuan diterima pada total `4` baris aktif Rina, yang pada batas `3` ditolak, sehingga nilai baru berlaku untuk transaksi baru

### Nilai 0 berarti Unlimited
53. Admin menyimpan Company default Assign dengan Max assets per assignee (concurrent) `0`
54. Admin mengajukan Assign aset `Toshiba Dynabook {runId}` kepada `Rina Kusuma {runId}`
55. Verifikasi pengajuan diterima walau Rina sudah memiliki `4` baris aktif, karena `0` berarti Unlimited

### Kuota dihitung per Category dari nilai efektif aset yang diajukan
56. Admin menyimpan Company default Assign dengan Max assets per assignee (concurrent) `3`
57. Admin menyimpan Category leaf `Laptop {runId}` dengan Max assets per assignee (concurrent) `1` sebagai nilai sendiri
58. Admin mengajukan Assign aset `Printer Canon G3010 {runId}` kepada `Maya Puspita {runId}`
59. Admin mengajukan Assign aset `Acer Aspire 5 {runId}` kepada `Maya Puspita {runId}`
60. Verifikasi pengajuan diterima karena kuota dihitung di Category `Laptop {runId}` saja: baris aktif Maya di Category itu `1` setelah baris baru, walau total lintas Category `2`
61. Admin mengajukan Assign aset `MacBook Air M2 {runId}` kepada `Maya Puspita {runId}`
62. Verifikasi pengajuan ditolak karena nilai kuota yang dipakai adalah nilai efektif aset yang diajukan, yaitu `1` dari Category leaf `Laptop {runId}` dan bukan `3` dari Company default: baris aktif Maya di Category itu menjadi `2`, sedangkan total lintas Category `3` masih di dalam batas `3`

### Deny pada override mengalahkan nilai lain dan Deny Category dievaluasi di server
63. Admin membuat override pada Group `Gudang Pusat {runId}` untuk transaksi Assign dengan Allow Assign `Allow`
64. Admin membuat override pada aset `Samsung Galaxy Book3 {runId}` untuk transaksi Assign dengan Allow Assign `Deny`
65. Admin mengajukan Assign aset `Samsung Galaxy Book3 {runId}` kepada `Tono Wibowo {runId}`
66. Verifikasi pengajuan ditolak walau override Group bernilai `Allow`, karena Deny pada override aset mengalahkan semua nilai lain
67. Admin menyimpan Category leaf `Monitor {runId}` dengan Allow Assign `Deny`
68. Admin mengirim pengajuan Assign aset `Monitor Dell P2422H {runId}` kepada `Tono Wibowo {runId}` langsung ke server tanpa melalui tampilan
69. Verifikasi pengajuan ditolak karena Deny pada Category tetap dievaluasi ulang di server

### Kombinasi efektif Allowed assignee OFF/OFF ditolak
70. Admin mengajukan Assign aset `Printer Scanner Fujitsu fi-7160 {runId}` kepada `Tono Wibowo {runId}`
71. Verifikasi pengajuan ditolak karena tidak ada tipe Assignee yang diizinkan: nilai efektif Allowed assignee: Employee `OFF` dan Allowed assignee: Division `OFF`, sedangkan nilai efektif Allow Assign bukan `Deny`

### Transaction timeout menutup transaksi Assign yang menunggu
72. Admin menyimpan Company default Assign dengan Require approval `ON`
73. Admin menyimpan Company default Assign dengan Transaction timeout `1`
74. `Tia Anggraini {runId}` mengajukan Assign aset `Printer Brother HL-L2375 {runId}` kepada `Tono Wibowo {runId}`, sehingga berstatus `Waiting for Approval`
75. `Tia Anggraini {runId}` mengajukan Assign aset `Printer Ricoh SP 111 {runId}` kepada `Tono Wibowo {runId}`
76. `Wawan Hidayat {runId}` menyetujui pengajuan Assign aset `Printer Ricoh SP 111 {runId}`, sehingga berstatus `Waiting for Handover`
77. Waktu berlalu 23 jam sejak kedua transaksi masuk statusnya
78. Background job pengecekan Transaction timeout berjalan
79. Verifikasi baris Assign aset `Printer Brother HL-L2375 {runId}` masih `Waiting for Approval` dan baris Assign aset `Printer Ricoh SP 111 {runId}` masih `Waiting for Handover`, karena batas Transaction timeout `1` hari sejak transaksi masuk status menunggu belum tercapai
80. Waktu berlalu sampai 1 hari sejak kedua transaksi masuk statusnya
81. Background job pengecekan Transaction timeout berjalan
82. Verifikasi baris Assign aset `Printer Brother HL-L2375 {runId}` berstatus `Canceled`
83. Verifikasi Note baris itu `Timed out (Waiting for Approval)`
84. Verifikasi log transaksi baris itu tercatat dengan Modified By `System`
85. Verifikasi baris Assign aset `Printer Ricoh SP 111 {runId}` berstatus `Canceled`
86. Verifikasi Note baris itu `Not handed over`
87. Verifikasi log transaksi baris itu tercatat dengan Modified By `System`
88. Verifikasi Draft Assign aset `HP ProBook 450 {runId}` tetap Draft dan tidak ditutup otomatis
89. Verifikasi baris Assign aset `Lenovo ThinkPad E14 {runId}` tetap berstatus `Assigned` dan tidak ditutup otomatis

### Approval dilewati saat Approval Workflow tidak tersedia di plan
90. Operator platform mengubah Approval Workflow pada plan entitas menjadi tidak tersedia, dengan Require approval tersimpan `ON`
91. `Tia Anggraini {runId}` mengajukan Assign aset `Printer Xerox B230 {runId}` kepada `Tono Wibowo {runId}`
92. Verifikasi pengajuan tidak berstatus `Waiting for Approval` melainkan `Waiting for Handover`, karena nilai efektif Require approval `OFF` untuk transaksi Assign

### Level Feature Suite Assignment Basic menetapkan Direct handover Deny
93. Operator platform mengubah level Feature Suite Assignment pada plan entitas menjadi `Basic`
94. Admin mengajukan Assign aset `Printer Kyocera ECOSYS {runId}` kepada `Tono Wibowo {runId}`
95. Verifikasi pengajuan Assign biasa diterima pada level `Basic`, karena yang tidak tersedia hanya Direct handover between holders
96. Admin mengajukan Reassign aset `Lenovo ThinkPad E14 {runId}` dari `Rina Kusuma {runId}` kepada `Tono Wibowo {runId}` melalui Direct handover between holders, dengan nilai tersimpan `Allow`
97. Verifikasi Reassign ditolak karena nilai efektif Direct handover between holders `Deny` pada level `Basic`, apa pun nilai tersimpan
98. Operator platform mengubah level Feature Suite Assignment pada plan entitas menjadi `Full`
99. Admin mengajukan Reassign aset `Lenovo ThinkPad E14 {runId}` dari `Rina Kusuma {runId}` kepada `Tono Wibowo {runId}` melalui Direct handover between holders
100. Verifikasi Reassign diterima karena nilai tersimpan `Allow` langsung berlaku saat level kembali `Full`

### Level Feature Suite Assignment None membuat Assign tidak tersedia
101. Operator platform mengubah level Feature Suite Assignment pada plan entitas menjadi `None`
102. Admin mengajukan Assign aset `Printer Samsung Xpress M2020 {runId}` kepada `Hendra Gunawan {runId}`
103. Verifikasi pengajuan ditolak karena pada level `None` Assign tidak tersedia

### Photo at start wajib pada Handover Assign dan Optional tanpa akseptasi
104. Operator platform mengubah level Feature Suite Assignment pada plan entitas menjadi `Full`
105. Admin menyimpan Company default Assign dengan Require approval `OFF`
106. Admin mengajukan Assign aset ber-tag `Printer Pantum P2500 {runId}` kepada `Hendra Gunawan {runId}`
107. Admin menjalankan langkah mulai Handover aset `Printer Pantum P2500 {runId}` dengan scan tag aset itu tanpa foto
108. Verifikasi langkah mulai ditolak karena Photo at start `ON` mewajibkan 1 foto pada langkah awal transaksi Assign, dan baris tetap berstatus `Waiting for Handover`
109. Admin menjalankan langkah mulai Handover aset `Printer Pantum P2500 {runId}` dengan satu foto dan scan tag aset itu
110. Verifikasi Handover selesai dan aset `Printer Pantum P2500 {runId}` berstatus `Assigned` kepada `Hendra Gunawan {runId}` tanpa akseptasi dari Assignee, karena Recipient acceptance `Optional` hanya menghilangkan langkah akseptasi saat handover

### Foto dan cek radius pada Unassign lewat I can't scan the TAG
111. Admin menyelesaikan Unassign aset `Asus Zenbook 14 {runId}` dari `Agus Hartono {runId}` lewat `I can't scan the TAG` dengan satu foto dari lokasi di dalam radius aset
112. Verifikasi foto yang disertakan tercatat pada transaksi Unassign aset `Asus Zenbook 14 {runId}`
113. Verifikasi pengecekan radius dijalankan atas Unassign aset `Asus Zenbook 14 {runId}`

### Kuota dari override All categories dihitung lintas Category
114. Admin membuat override pada Group `Gudang Cabang Lintas {runId}` di All categories untuk transaksi Assign dengan Max assets per assignee (concurrent) `2`
115. Admin mengajukan Assign aset `Scanner Epson DS-530 {runId}` kepada `Bagus Prasetyo {runId}`
116. Admin mengajukan Assign aset `Proyektor Epson EB-X06 {runId}` kepada `Bagus Prasetyo {runId}`
117. Verifikasi kedua pengajuan diterima pada total `2` baris aktif Bagus, tepat di batas `2` dari override All categories
118. Admin mengajukan Assign aset `Kamera Canon EOS 200D {runId}` kepada `Bagus Prasetyo {runId}`
119. Verifikasi pengajuan ditolak karena nilai `2` bersumber dari override ber-Category All categories sehingga kuota dihitung lintas Category: total `3` baris aktif Bagus melebihi `2`, walau baris aktif di Category `Kamera {runId}` saja hanya `1`
120. Verifikasi tidak ada baris Assign baru untuk aset `Kamera Canon EOS 200D {runId}` dan jumlah baris aktif Bagus tetap `2`

### Kuota dari override Category leaf dihitung di Category itu
121. Admin membuat override pada Group `Gudang Cabang Leaf {runId}` di Category `Kamera {runId}` untuk transaksi Assign dengan Max assets per assignee (concurrent) `1`
122. Admin mengajukan Assign aset `Proyektor BenQ MX560 {runId}` kepada `Citra Dewi {runId}`
123. Admin mengajukan Assign aset `Kamera Nikon D3500 {runId}` kepada `Citra Dewi {runId}`
124. Verifikasi pengajuan aset `Kamera Nikon D3500 {runId}` diterima karena nilai `1` bersumber dari override ber-Category leaf `Kamera {runId}` sehingga kuota dihitung di Category itu saja: baris aktif Citra di Category itu `1` setelah baris baru, walau total lintas Category `2`
125. Admin mengajukan Assign aset `Kamera Sony ZV-E10 {runId}` kepada `Citra Dewi {runId}`
126. Verifikasi pengajuan aset `Kamera Sony ZV-E10 {runId}` ditolak karena baris aktif Citra di Category `Kamera {runId}` menjadi `2`, melebihi nilai `1` dari override ber-Category leaf

### Baris Waiting for Approval ikut dihitung sebagai baris aktif
127. Operator platform mengubah Approval Workflow pada plan entitas menjadi tersedia
128. Admin menyimpan Company default Assign dengan Require approval `ON`
129. Admin menyimpan Company default Assign dengan Max assets per assignee (concurrent) `1`
130. `Tia Anggraini {runId}` mengajukan Assign aset `Printer HP LaserJet M111 {runId}` kepada `Wulan Safitri {runId}`, sehingga berstatus `Waiting for Approval`
131. `Tia Anggraini {runId}` mengajukan Assign aset `Printer Lexmark MS431 {runId}` kepada `Wulan Safitri {runId}`
132. Verifikasi pengajuan aset `Printer Lexmark MS431 {runId}` ditolak karena baris `Waiting for Approval` milik `Wulan Safitri {runId}` ikut dihitung sebagai baris aktif: total `2` baris aktif melebihi batas `1`
133. Verifikasi tidak ada baris Assign baru untuk aset `Printer Lexmark MS431 {runId}` dan baris aset `Printer HP LaserJet M111 {runId}` tetap `Waiting for Approval`

