---
id: TC-FA-FATR-BE-107-approval-disposal-dep-disposal
title: "Approval dan penentuan approver pada transaksi Disposal"
layer: be-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules:
  - "§Aturan Logika Modul#r74"
  - "§Aturan Logika Modul#r81"
  - "§4.1#r186"
  - "§4.1#r188"
  - "§4.1#r189"
  - "§4.1#r193"
  - "§4.1#r194"
  - "§4.1#r195"
  - "§4.1#r196"
  - "§9.2#b379"
  - "§9.2#b380"
  - "§9.2#b381"
  - "§9.2#b382"
  - "§9.2#b441"
  - "§9.2#b443"
  - "§9.2#b444"
  - "§9.2#b445"
  - "§9.2#b446"
  - "§9.2#b448"
  - "§9.2#b449"
  - "§9.2#b450"
  - "§9.2#b451"
  - "§9.2#b453"
  - "§9.2#b455"
  - "§9.2#b456"
  - "§9.2#b457"
  - "§9.2#b458"
  - "§9.2#b460"
  - "§9.2#b461"
  - "§9.2#b464"
  - "§9.2#b465"
  - "§9.2#b466"
  - "§9.2#b468"
  - "§9.2#b469"
  - "§9.2#b470"
  - "§9.2#b471"
  - "§9.2#b472"
  - "§9.2#b475"
  - "§9.2#b476"
  - "§9.2#b477"
  - "§9.2#b488"
  - "§9.2#b489"
  - "§9.2#b490"
  - "§9.2#b491"
  - "§9.2#b492"
  - "§9.2#b493"
  - "§9.2#b494"
  - "§9.2#b463"
  - "§9.2#b479"
  - "§9.2#b480"
  - "§9.2#b483"
  - "§9.2#b481"
  - "§9.2#b482"
  - "§9.2#b527"
  - "§9.2#b528"
  - "§9.2#b530"
  - "§9.2#b534"
  - "§9.2#b535"
  - "§9.2#b537"
  - "§9.2#b538"
  - "§9.2#b540"
  - "§9.2#b541"
  - "§9.2#b549"
  - "§9.2#b550"
  - "§9.2#b551"
  - "§9.2#b552"
  - "§9.2#b553"
  - "§9.2#b555"
  - "§9.2#b547"
  - "§9.4.1#r20"
  - "§9.4.2#r37"
  - "§9.4.2#r40"
  - "§9.4.2#r42"
  - "§9.4.2#r130"
  - "§9.4.2#r131"
  - "§9.4.2#r136"
  - "§9.4.2#r138"
  - "§9.4.2#r148"
  - "§9.4.2#r149"
  - "§9.4.2#r150"
  - "§9.4.2#r152"
  - "§9.4.3#b4"
  - "§9.4.4#r11"
  - "§9.4.4#r48"
  - "§9.4.4#r49"
  - "§9.4.4#r50"
  - "§9.4.4#r53"
  - "§9.8#r10"
  - "§9.8#r11"
  - "§9.8#r12"
  - "§9.10.1#r11"
  - "§9.10.1#r12"
  - "§10#b1"
smoke: []
dependsOn:
  - "Disposal: pengajuan, approval, dan Execute"
owner: BE
trace:
  "§Aturan Logika Modul#r74": 97
  "§Aturan Logika Modul#r81": 100
  "§4.1#r186": 85
  "§4.1#r188": 87
  "§4.1#r189": [88, 90]
  "§4.1#r193": [10, 22]
  "§4.1#r194": [10, 15]
  "§4.1#r195": [24, 26, 30]
  "§4.1#r196": [11, 15, 30, 31]
  "§9.2#b379": [79, 81, 105, 106, 108, 109, 116, 117]
  "§9.2#b380": [2, 85]
  "§9.2#b381": [3, 6, 7]
  "§9.2#b382": 97
  "§9.2#b441": 12
  "§9.2#b443": [10, 24, 50]
  "§9.2#b444": 3
  "§9.2#b445": [95, 96]
  "§9.2#b446": [2, 98]
  "§9.2#b448": [3, 4]
  "§9.2#b449": 4
  "§9.2#b450": 9
  "§9.2#b451": 64
  "§9.2#b453": [34, 63]
  "§9.2#b455": [10, 22]
  "§9.2#b456": [10, 15]
  "§9.2#b457": [24, 26, 30]
  "§9.2#b458": [11, 15, 16, 30, 31]
  "§9.2#b460": 37
  "§9.2#b461": [37, 42, 45]
  "§9.2#b464": 48
  "§9.2#b465": [92, 94]
  "§9.2#b466": 40
  "§9.2#b468": [53, 58]
  "§9.2#b469": [53, 56]
  "§9.2#b470": 50
  "§9.2#b471": 51
  "§9.2#b472": [55, 61]
  "§9.2#b475": [63, 71]
  "§9.2#b476": 65
  "§9.2#b477": 66
  "§9.2#b488": [63, 114]
  "§9.2#b489": 71
  "§9.2#b490": [73, 77]
  "§9.2#b491": [73, 74]
  "§9.2#b492": 77
  "§9.2#b493": 27
  "§9.2#b494": [34, 35]
  "§9.2#b463": [38, 46]
  "§9.2#b479": [66, 69, 102]
  "§9.2#b480": 102
  "§9.2#b483": 103
  "§9.2#b481": [66, 67]
  "§9.2#b482": 69
  "§9.2#b527": 83
  "§9.2#b528": 85
  "§9.2#b530": [87, 112]
  "§9.2#b534": [10, 22]
  "§9.2#b535": [11, 16, 26]
  "§9.2#b537": 50
  "§9.2#b538": 50
  "§9.2#b540": [63, 71]
  "§9.2#b541": 66
  "§9.2#b549": [37, 42, 45]
  "§9.2#b550": [37, 42, 45]
  "§9.2#b551": [38, 43]
  "§9.2#b552": 46
  "§9.2#b553": [39, 43, 46]
  "§9.2#b555": [92, 94]
  "§9.2#b547": 85
  "§9.4.1#r20": [58, 59]
  "§9.4.2#r37": [97, 98]
  "§9.4.2#r40": [50, 51]
  "§9.4.2#r42": [19, 20]
  "§9.4.2#r130": [63, 71]
  "§9.4.2#r131": 65
  "§9.4.2#r136": 85
  "§9.4.2#r138": [88, 90]
  "§9.4.2#r148": [37, 42, 45]
  "§9.4.2#r149": [38, 43, 46]
  "§9.4.2#r150": [39, 43, 46]
  "§9.4.2#r152": [92, 94]
  "§9.4.3#b4": [53, 58]
  "§9.4.4#r11": 65
  "§9.4.4#r48": [19, 20]
  "§9.4.4#r49": [50, 51]
  "§9.4.4#r50": [63, 65, 66]
  "§9.4.4#r53": [37, 45, 92, 94]
  "§9.8#r10": [51, 52]
  "§9.8#r11": [38, 39, 46]
  "§9.8#r12": 65
  "§9.10.1#r11": 99
  "§9.10.1#r12": [99, 101]
  "§10#b1": 12
---

# Approval dan penentuan approver pada transaksi Disposal

## Prerequisites
- Aktor: Pengaju Disposal `Rina Wijaya {runId}`. Aktor lain yang memutuskan atau memicu perubahan: Approver `Budi Santoso {runId}`, `Citra Lestari {runId}`, dan `Dedi Kurnia {runId}`, Group Manager `Gita Maharani {runId}` dan `Hendra Saputra {runId}`, Total Control `Tono Prasetyo {runId}` dan `Umar Hakim {runId}`, Aktor Disposal `Indra Pratama {runId}`, Staff Disposal `Sari Wulandari {runId}`, Group Manager `Maya Anggraini {runId}`, dan Accounting `Joko Susilo {runId}`.
- Data:
  - DU-107-1: Group `Divisi Operasional {runId}`
  - DU-107-2: Group `Workshop Operasional {runId}`, Group induk `Divisi Operasional {runId}`
  - DU-107-3: Group `Divisi Lain {runId}`
  - DU-107-4: Group `Divisi Gudang {runId}`
  - DU-107-5: Group `Divisi Mandiri {runId}`
  - DU-107-6: Group `Divisi Bersama {runId}`
  - DU-107-7: Group `Divisi Satu Orang {runId}`
  - DU-107-8: Group `Divisi Tanpa Manajer {runId}`
  - DU-107-9: Category `Kendaraan Operasional OR {runId}`, Require approval `ON`, Approval type `Any one approver`
  - DU-107-10: Category `Kendaraan Operasional AND {runId}`, Require approval `ON`, Approval type `All approvers (AND)`
  - DU-107-11: Category `Kendaraan Tanpa Approval {runId}`, Require approval `OFF`, Approval type `Any one approver`
  - DU-107-13: User `Rina Wijaya {runId}`, Role `Pengaju Disposal dan Role Transaksi Approver Disposal pada Divisi Mandiri dan Divisi Bersama`, Cakupan `Workshop Operasional {runId}, Divisi Gudang {runId}, Divisi Mandiri {runId}, Divisi Bersama {runId}, Divisi Tanpa Manajer {runId}, Divisi Satu Orang {runId}, Sub Gudang Utara {runId}`, Status `Aktif`
  - DU-107-14: User `Budi Santoso {runId}`, Role `Role Transaksi Approver Disposal`, Cakupan `Divisi Operasional {runId} beserta descendant, Divisi Bersama {runId}`, Status `Aktif`
  - DU-107-15: User `Citra Lestari {runId}`, Role `Role Transaksi Approver Disposal`, Cakupan `Workshop Operasional {runId}`, Status `Aktif`
  - DU-107-16: User `Dedi Kurnia {runId}`, Role `Role Transaksi Approver Disposal`, Cakupan `Divisi Lain {runId}`, Status `Aktif`
  - DU-107-17: User `Eko Nugroho {runId}`, Role `Role Transaksi Approver Disposal`, Cakupan `Divisi Gudang {runId}`, Status `Nonaktif`
  - DU-107-18: User `Fajar Hidayat {runId}`, Role `Role Transaksi Approver Disposal dengan tingkat akses Read Only`, Cakupan `Divisi Gudang {runId}`, Status `Aktif`
  - DU-107-19: User `Gunawan Wibowo {runId}`, Role `Role Transaksi Approver Disposal tanpa lisensi addon`, Cakupan `Divisi Gudang {runId}`, Status `Aktif`
  - DU-107-20: User `Gita Maharani {runId}`, Role `Group Manager tanpa penugasan Approver pada Divisi Operasional, dan Group Manager sekaligus Role Transaksi Approver Disposal pada Divisi Satu Orang`, Cakupan `Divisi Operasional {runId} beserta descendant, Divisi Satu Orang {runId}`, Status `Aktif`
  - DU-107-21: User `Hendra Saputra {runId}`, Role `Group Manager tanpa penugasan Approver`, Cakupan `Divisi Gudang {runId}`, Status `Aktif`
  - DU-107-22: User `Tono Prasetyo {runId}`, Role `Total Control`, Cakupan `seluruh entitas`, Status `Aktif`
  - DU-107-23: User `Umar Hakim {runId}`, Role `Total Control`, Cakupan `seluruh entitas`, Status `Aktif`
  - DU-107-24: User `Indra Pratama {runId}`, Role `Aktor Disposal`, Cakupan `Workshop Operasional {runId}`, Status `Aktif`
  - DU-107-25: User `Joko Susilo {runId}`, Role `Accounting`, Cakupan `seluruh entitas`, Status `Aktif`
  - DU-107-26: Asset `Truk Boks T1 {runId}`, Category `Kendaraan Operasional OR {runId}`, Group `Workshop Operasional {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-27: Asset `Truk Boks T2 {runId}`, Category `Kendaraan Operasional OR {runId}`, Group `Workshop Operasional {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-28: Asset `Truk Boks T3 {runId}`, Category `Kendaraan Operasional OR {runId}`, Group `Workshop Operasional {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-29: Asset `Truk Boks T4 {runId}`, Category `Kendaraan Operasional AND {runId}`, Group `Workshop Operasional {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-30: Asset `Truk Boks T5 {runId}`, Category `Kendaraan Operasional AND {runId}`, Group `Workshop Operasional {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-31: Asset `Truk Boks T6 {runId}`, Category `Kendaraan Operasional AND {runId}`, Group `Workshop Operasional {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-32: Asset `Truk Boks T8 {runId}`, Category `Kendaraan Operasional OR {runId}`, Group `Workshop Operasional {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-33: Asset `Truk Boks T9 {runId}`, Category `Kendaraan Operasional OR {runId}`, Group `Workshop Operasional {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-34: Asset `Truk Gudang G1 {runId}`, Category `Kendaraan Operasional OR {runId}`, Group `Divisi Gudang {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-35: Asset `Truk Satu Orang U1 {runId}`, Category `Kendaraan Operasional OR {runId}`, Group `Divisi Satu Orang {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-36: Asset `Truk Mandiri S1 {runId}`, Category `Kendaraan Operasional OR {runId}`, Group `Divisi Mandiri {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-37: Asset `Truk Bersama S2 {runId}`, Category `Kendaraan Operasional OR {runId}`, Group `Divisi Bersama {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-38: Asset `Truk Gudang G2 {runId}`, Category `Kendaraan Operasional OR {runId}`, Group `Divisi Gudang {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-39: Asset `Truk Gudang G3 {runId}`, Category `Kendaraan Operasional OR {runId}`, Group `Divisi Gudang {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-40: Asset `Truk Tanpa Manajer V1 {runId}`, Category `Kendaraan Operasional OR {runId}`, Group `Divisi Tanpa Manajer {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-41: Asset `Truk Tanpa Manajer V2 {runId}`, Category `Kendaraan Operasional AND {runId}`, Group `Divisi Tanpa Manajer {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-42: Asset `Truk Tanpa Approval Z1 {runId}`, Category `Kendaraan Tanpa Approval {runId}`, Group `Workshop Operasional {runId}`, Tag `Ber-tag`, Condition `Active`, Reason `Aset rusak berat`
  - DU-107-43: Asset `Truk Tanpa Approval Z2 {runId}`, Category `Kendaraan Tanpa Approval {runId}`, Group `Workshop Operasional {runId}`, Tag `Ber-tag`, Condition `Active`, Reason `Aset rusak berat`
  - DU-107-44: Asset `Truk Tanpa Approval Z3 {runId}`, Category `Kendaraan Tanpa Approval {runId}`, Group `Workshop Operasional {runId}`, Tag `Ber-tag`, Condition `Active`, Reason `Aset rusak berat`
  - DU-107-45: Asset `Truk Hilang X1 {runId}`, Category `Kendaraan Operasional OR {runId}`, Group `Workshop Operasional {runId}`, Tag `Ber-tag`, Condition `Missing`
  - DU-107-46: Asset `Truk Dilarang X2 {runId}`, Category `Kendaraan Operasional OR {runId}`, Group `Workshop Operasional {runId}`, Tag `Ber-tag`, Condition `Active`, Asset override Allow Disposal `Deny`
  - DU-107-54: Category `Kendaraan Terbatas {runId}`, Require approval `ON`, Approval type `Any one approver`, Allowed disposal types `Sell`
  - DU-107-55: Asset `Truk Terbatas L1 {runId}`, Category `Kendaraan Terbatas {runId}`, Group `Workshop Operasional {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-56: Asset `Truk Hilang Dilarang X3 {runId}`, Category `Kendaraan Operasional OR {runId}`, Group `Workshop Operasional {runId}`, Tag `Ber-tag`, Condition `Missing`, Asset override Allow Disposal `Deny`
  - DU-107-57: Asset `Truk Tanpa Approval Z4 {runId}`, Category `Kendaraan Tanpa Approval {runId}`, Group `Workshop Operasional {runId}`, Tag `Ber-tag`, Condition `Active`, Reason `Aset rusak berat`
  - DU-107-58: User `Sari Wulandari {runId}`, Role `Staff Disposal`, Cakupan `Workshop Operasional {runId}`, Status `Aktif`
  - DU-107-59: Group `Sub Gudang Utara {runId}`, Group induk `Divisi Gudang {runId}`
  - DU-107-60: User `Maya Anggraini {runId}`, Role `Group Manager tanpa penugasan Approver`, Cakupan `Sub Gudang Utara {runId}`, Status `Aktif`
  - DU-107-61: Asset `Truk Sub Gudang S3 {runId}`, Category `Kendaraan Operasional OR {runId}`, Group `Sub Gudang Utara {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-107-62: Asset `Truk Terbatas L2 {runId}`, Category `Kendaraan Terbatas {runId}`, Group `Workshop Operasional {runId}`, Tag `Ber-tag`, Condition `Active`, Asset override Allow Disposal `Deny`
- Kondisi:
  - Require approval Disposal pada Category uji bernilai sesuai entri data, Approval type default Company bernilai `Any one approver`, Transaction timeout Disposal bernilai `7` (days), Approval Workflow tersedia di plan entitas aktor, dan Accounting & Depreciation (FA-7) aktif di plan entitas aktor sehingga tahap Post tersedia.
  - Group Manager `Gita Maharani {runId}` dan `Hendra Saputra {runId}` aktif. Tidak ada Group Manager aktif yang menaungi Group `Divisi Tanpa Manajer {runId}` di node itu maupun ancestor-nya. `Tono Prasetyo {runId}` dan `Umar Hakim {runId}` aktif.

## Test Steps

### Any one approver: persetujuan satu Approver di Group induk cukup dan Approver lain Not Involved
1. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Boks T1 {runId}` dengan scan tag aset
2. Verifikasi Disposal memerlukan approval dan berstatus `Waiting for Approval` karena Require approval Category bernilai `ON` dan Approval Workflow tersedia di plan
3. Verifikasi `Citra Lestari {runId}` menjadi Approver karena ditugaskan Role Transaksi `Approver` pada Group aset `Workshop Operasional {runId}`
4. Verifikasi `Budi Santoso {runId}` menjadi Approver untuk aset di Group turunan karena penugasannya pada Group induk `Divisi Operasional {runId}` mencakup seluruh descendant
5. `Dedi Kurnia {runId}` mencoba menyetujui Disposal atas `Truk Boks T1 {runId}`
6. Verifikasi percobaan `Dedi Kurnia {runId}` ditolak karena Role Transaksi `Approver`-nya ditugaskan pada Group yang tidak mencakup Group aset
7. Verifikasi Disposal tetap berstatus `Waiting for Approval` setelah percobaan `Dedi Kurnia {runId}`
8. `Budi Santoso {runId}` menyetujui Disposal atas `Truk Boks T1 {runId}`
9. Verifikasi keputusan `Budi Santoso {runId}` diterima langsung tanpa langkah eskalasi tersendiri meski ia ditugaskan pada Group induk
10. Verifikasi Disposal berstatus `Waiting for Execution` karena Approval type `Any one approver` memakai rule OR dan satu persetujuan cukup
11. Verifikasi status `Citra Lestari {runId}` pada Disposal menjadi `Not Involved` menurut aturan keputusan Approval type
12. Verifikasi tidak ada level approval lanjutan sesudah persetujuan itu karena approval hanya satu level atas satu transaksi

### Any one approver: penolakan satu Approver langsung menolak Disposal
13. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Boks T2 {runId}` dengan scan tag aset
14. `Citra Lestari {runId}` menolak Disposal atas `Truk Boks T2 {runId}`
15. Verifikasi Disposal berstatus `Rejected` karena Approval type `Any one approver` memakai rule OR dan satu penolakan cukup
16. Verifikasi status `Budi Santoso {runId}` pada Disposal menjadi `Not Involved`

### Any one approver: keputusan beberapa Approver hampir bersamaan ditentukan satu keputusan
17. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Boks T3 {runId}` dengan scan tag aset
18. `Budi Santoso {runId}` menyetujui dan `Citra Lestari {runId}` menolak Disposal atas `Truk Boks T3 {runId}` hampir bersamaan
19. Verifikasi Disposal berstatus akhir `Waiting for Execution` atau `Rejected` sesuai tepat satu keputusan yang diterima server lebih dulu
20. Verifikasi Approver yang keputusannya tidak ditetapkan menjadi `Not Involved` dan permintaannya ditutup

### All approvers (AND): semua Approver harus menyetujui dan Group Manager tanpa penugasan tidak dihitung
21. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Boks T4 {runId}` dengan scan tag aset
22. Verifikasi Approval type `All approvers (AND)` berlaku karena ada lebih dari satu Approver pada Disposal
23. `Budi Santoso {runId}` menyetujui Disposal atas `Truk Boks T4 {runId}`
24. Verifikasi Disposal tetap berstatus `Waiting for Approval` karena rule AND menunggu Approver lain
25. `Citra Lestari {runId}` menyetujui Disposal atas `Truk Boks T4 {runId}`
26. Verifikasi Disposal berstatus `Waiting for Execution` sesudah semua Approver menyetujui
27. Verifikasi persetujuan selesai tanpa keputusan `Gita Maharani {runId}`, Group Manager yang eligible tanpa penugasan Approver, karena ia tidak dihitung dalam rule AND

### All approvers (AND): penolakan satu Approver langsung menolak Disposal
28. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Boks T5 {runId}` dengan scan tag aset
29. `Budi Santoso {runId}` menolak Disposal atas `Truk Boks T5 {runId}`
30. Verifikasi Disposal berstatus `Rejected` walaupun Approval type `All approvers (AND)`
31. Verifikasi status `Citra Lestari {runId}` pada Disposal menjadi `Not Involved`

### Group Manager tanpa penugasan tetap memutuskan secara override final meski ada Approver terdaftar
32. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Boks T6 {runId}` dengan scan tag aset
33. `Gita Maharani {runId}` menyetujui Disposal atas `Truk Boks T6 {runId}`
34. Verifikasi Disposal langsung berstatus `Waiting for Execution` tanpa menunggu `Budi Santoso {runId}` dan `Citra Lestari {runId}` karena Group Manager yang menaungi Group aset eligible menyetujui tanpa penugasan Approver
35. Verifikasi status `Budi Santoso {runId}` dan `Citra Lestari {runId}` pada Disposal menjadi `Not Involved`

### Pengaju Group Manager atau Total Control melewati seluruh langkah approval
36. `Gita Maharani {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Boks T8 {runId}` dengan scan tag aset
37. Verifikasi Disposal langsung disetujui tanpa langkah approval dan berstatus `Waiting for Execution` walaupun `Budi Santoso {runId}` dan `Citra Lestari {runId}` terdaftar sebagai Approver
38. Verifikasi log transaksi mencatat `Approved by Gita Maharani {runId} (Group Manager — requester)` karena pengaju Group Manager yang menaungi Group aset di ancestor-nya
39. Verifikasi Modified By log itu adalah `Gita Maharani {runId}`, bukan `System`
40. Verifikasi `Gita Maharani {runId}` tidak menjadi approver transaksinya sendiri walaupun melewati approval
41. `Hendra Saputra {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Gudang G1 {runId}` dengan scan tag aset
42. Verifikasi Disposal langsung disetujui tanpa langkah approval dan berstatus `Waiting for Execution` karena pengaju Group Manager yang menaungi Group aset di node itu
43. Verifikasi log transaksi mencatat `Approved by Hendra Saputra {runId} (Group Manager — requester)` dengan Modified By `Hendra Saputra {runId}`
44. `Tono Prasetyo {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Boks T9 {runId}` dengan scan tag aset
45. Verifikasi Disposal langsung disetujui tanpa langkah approval dan berstatus `Waiting for Execution` karena pengaju Total Control
46. Verifikasi log transaksi mencatat `Approved by Tono Prasetyo {runId} (Total Control — requester)` dengan Modified By `Tono Prasetyo {runId}`
47. `Gita Maharani {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Satu Orang U1 {runId}` dengan scan tag aset
48. Verifikasi log transaksi mencatat `Approved by Gita Maharani {runId} (Group Manager — requester)`, bukan `Approved by system (no independent approver)`, walaupun pengaju juga satu-satunya Approver terdaftar, karena Kondisi A dievaluasi lebih dulu daripada self-approval guard

### Pengaju satu-satunya Approver eligible: approval dilewati dan dicatat oleh System
49. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Mandiri S1 {runId}` dengan scan tag aset
50. Verifikasi langkah approval dilewati dan Disposal langsung disetujui dan berstatus `Waiting for Execution` karena pengaju satu-satunya Approver eligible
51. Verifikasi log transaksi mencatat `Approved by system (no independent approver)`
52. Verifikasi Modified By log itu adalah `System`
53. Verifikasi `Rina Wijaya {runId}` tidak menjadi approver transaksinya sendiri

### Pengaju dikecualikan dari daftar Approver dan approval berjalan dengan Approver lain
54. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Bersama S2 {runId}` dengan scan tag aset
55. Verifikasi Disposal berstatus `Waiting for Approval` dan approval berjalan dengan `Budi Santoso {runId}` karena sebagian Approver eligible bukan pengaju
56. Verifikasi daftar Approver Disposal tidak memuat `Rina Wijaya {runId}` sebagai pengaju
57. `Rina Wijaya {runId}` mencoba menyetujui Disposal atas `Truk Bersama S2 {runId}`
58. Verifikasi percobaan `Rina Wijaya {runId}` ditolak karena pengaju tidak pernah menjadi approver transaksinya sendiri
59. Verifikasi Disposal tetap berstatus `Waiting for Approval`
60. `Budi Santoso {runId}` menyetujui Disposal atas `Truk Bersama S2 {runId}`
61. Verifikasi Disposal berstatus `Waiting for Execution` sesudah persetujuan `Budi Santoso {runId}`

### Tidak ada Approver eligible: rute jatuh ke Group Manager yang menaungi Group aset
62. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Gudang G2 {runId}` dengan scan tag aset
63. Verifikasi Approver Disposal adalah `Hendra Saputra {runId}`, Group Manager yang menaungi Group aset, karena tidak ada Approver eligible yang mencakup Group aset
64. Verifikasi `Eko Nugroho {runId}` yang nonaktif, `Fajar Hidayat {runId}` dengan tingkat akses Read Only, dan `Gunawan Wibowo {runId}` tanpa lisensi addon tidak dihitung sebagai Approver eligible
65. Verifikasi log transaksi mencatat rute itu dengan Modified By `System` dan tanpa Note enum
66. Verifikasi satu notifikasi `approver_required` terkirim untuk Disposal atas `Truk Gudang G2 {runId}`
67. Verifikasi jumlah notifikasi `approver_required` untuk Disposal atas `Truk Gudang G2 {runId}` bertambah tepat satu dibanding sebelum pengajuan
68. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Gudang G3 {runId}` dengan scan tag aset
69. Verifikasi Disposal atas `Truk Gudang G3 {runId}` mengirim notifikasi `approver_required` sendiri, terpisah dari Disposal atas `Truk Gudang G2 {runId}`

### Tidak ada Approver eligible dan tidak ada Group Manager aktif: rute jatuh ke Total Control
70. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Tanpa Manajer V1 {runId}` dengan scan tag aset
71. Verifikasi approver fallback Disposal memuat `Tono Prasetyo {runId}` dan `Umar Hakim {runId}` karena tidak ada Approver eligible dan tidak ada Group Manager aktif yang menaungi Group aset
72. `Tono Prasetyo {runId}` menyetujui Disposal atas `Truk Tanpa Manajer V1 {runId}`
73. Verifikasi Disposal berstatus `Waiting for Execution` karena Approval type `Any one approver` berlaku pada himpunan fallback dan salah satu cukup
74. Verifikasi status `Umar Hakim {runId}` pada Disposal menjadi `Not Involved`
75. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Tanpa Manajer V2 {runId}` dengan scan tag aset
76. `Tono Prasetyo {runId}` menyetujui Disposal atas `Truk Tanpa Manajer V2 {runId}`
77. Verifikasi Disposal tetap berstatus `Waiting for Approval` karena Approval type `All approvers (AND)` berlaku pada himpunan fallback dan semua harus menyetujui

### Approval dievaluasi paling akhir sesudah aturan tetap dan Deny pada override
78. `Rina Wijaya {runId}` mengajukan Disposal jenis `Sell` atas `Truk Hilang X1 {runId}` dengan scan tag aset
79. Verifikasi pengajuan ditolak oleh aturan tetap dan tidak ada permintaan approval yang diterima `Budi Santoso {runId}` maupun `Citra Lestari {runId}`
80. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Dilarang X2 {runId}` dengan scan tag aset
81. Verifikasi pengajuan ditolak karena override bernilai Deny dan tidak ada permintaan approval yang diterima `Budi Santoso {runId}` maupun `Citra Lestari {runId}`

### Disposal tanpa approval karena Require approval OFF: alasan wajib, langsung menunggu Execute, Accounting tetap Post
82. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Tanpa Approval Z1 {runId}` dengan scan tag aset, tanpa Reason
83. Verifikasi pengajuan ditolak karena Reason wajib diisi pada Disposal dengan Require approval OFF
84. `Rina Wijaya {runId}` mengajukan ulang Disposal jenis `Scrap` atas `Truk Tanpa Approval Z1 {runId}` dengan scan tag aset dan Reason `Aset rusak berat`
85. Verifikasi Disposal langsung berstatus `Waiting for Execution` tanpa melewati `Waiting for Approval` karena nilai efektif Require approval OFF
86. `Indra Pratama {runId}` melakukan Execute atas Disposal `Truk Tanpa Approval Z1 {runId}`
87. Verifikasi Disposal menjadi Executed saat Execute oleh Aktor Disposal
88. Verifikasi Disposal berstatus Executed menunggu posting dan belum selesai sampai Post dilakukan oleh `Joko Susilo {runId}`
89. `Joko Susilo {runId}` melakukan Post atas Disposal `Truk Tanpa Approval Z1 {runId}`
90. Verifikasi Post oleh `Joko Susilo {runId}` diterima server, dan data serta log transaksi Disposal sesudahnya mencatat Post itu

### Kondisi A tidak berlaku bila Require approval efektif OFF
91. `Gita Maharani {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Tanpa Approval Z2 {runId}` dengan scan tag aset dan Reason `Aset rusak berat`
92. Verifikasi Disposal berstatus `Waiting for Execution` dan log transaksi tidak memuat `Approved by Gita Maharani {runId} (Group Manager — requester)`
93. `Tono Prasetyo {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Tanpa Approval Z3 {runId}` dengan scan tag aset dan Reason `Aset rusak berat`
94. Verifikasi Disposal berstatus `Waiting for Execution` dan log transaksi tidak memuat `Approved by Tono Prasetyo {runId} (Total Control — requester)`

### Batas Transaction timeout per transaksi berlaku untuk status Waiting for Approval
95. Verifikasi Disposal berstatus `Waiting for Approval` yang belum melewati batas Transaction timeout Disposal `7` hari tetap berstatus `Waiting for Approval`
96. Verifikasi Disposal berstatus `Waiting for Approval` yang melewati batas Transaction timeout Disposal `7` hari berstatus `Canceled`

### Approval Workflow tidak tersedia di plan: approval dilewati dan Disposal berjalan seperti Require approval OFF
97. Verifikasi langkah approval dilewati bila Approval Workflow tidak tersedia di plan, walaupun Require approval Category bernilai `ON`
98. Verifikasi nilai efektif Require approval OFF dan approval hanya berlaku bila Approval Workflow tersedia di plan
99. Verifikasi Disposal langsung berstatus `Waiting for Execution` tanpa melewati `Waiting for Approval` bila Approval Workflow tidak tersedia di plan, seperti Disposal dengan Require approval OFF
100. Verifikasi penugasan Role Transaksi `Approver` tidak dipakai selama Approval Workflow tidak tersedia di plan, sehingga Approver tidak menerima permintaan approval
101. Verifikasi pengajuan Disposal tanpa Reason ditolak karena Reason wajib diisi pada Disposal yang berjalan seperti Require approval OFF saat Approval Workflow tidak tersedia di plan

### Notifikasi approver_required terkirim saat Save menimbulkan kondisi tanpa Approver dan tidak diulang
102. Verifikasi notifikasi `approver_required` terkirim bila Save konfigurasi Approval menimbulkan kondisi tidak ada Role Transaksi `Approver` yang ditugaskan untuk suatu transaksi
103. Verifikasi notifikasi `approver_required` momen Save konfigurasi Approval tidak diulang selama konfigurasi Approval tidak diubah

### Aturan tetap dan Eligibility dievaluasi sebelum Approval
104. `Rina Wijaya {runId}` mengajukan Disposal jenis `Sell` atas `Truk Hilang Dilarang X3 {runId}` dengan scan tag aset
105. Verifikasi pengajuan ditolak oleh aturan tetap aset berkondisi `Missing` yang hanya dapat di-Disposal jenis `Lost` atau `Write-off`, bukan oleh Deny pada override
106. Verifikasi tidak ada permintaan approval yang diterima `Budi Santoso {runId}` maupun `Citra Lestari {runId}` untuk aset `Truk Hilang Dilarang X3 {runId}`
107. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Terbatas L1 {runId}` dengan scan tag aset
108. Verifikasi pengajuan ditolak karena jenis `Scrap` tidak ada di Allowed disposal types `Sell` Category `Kendaraan Terbatas {runId}`
109. Verifikasi tidak ada permintaan approval yang diterima `Budi Santoso {runId}` maupun `Citra Lestari {runId}` untuk aset `Truk Terbatas L1 {runId}`

### Disposal tanpa approval: Staff Disposal dapat melakukan Execute
110. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Tanpa Approval Z4 {runId}` dengan scan tag aset dan Reason `Aset rusak berat`
111. `Sari Wulandari {runId}` melakukan Execute atas Disposal `Truk Tanpa Approval Z4 {runId}`
112. Verifikasi Disposal `Truk Tanpa Approval Z4 {runId}` menjadi Executed saat Execute oleh Staff Disposal

### Tidak ada Approver eligible: approver fallback memuat semua Group Manager di node dan ancestor Group aset
113. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Sub Gudang S3 {runId}` dengan scan tag aset
114. Verifikasi approver fallback Disposal atas `Truk Sub Gudang S3 {runId}` memuat `Maya Anggraini {runId}`, Group Manager yang menaungi Group aset `Sub Gudang Utara {runId}` di node itu, dan `Hendra Saputra {runId}`, Group Manager yang menaungi Group induk `Divisi Gudang {runId}` sebagai ancestor, karena tidak ada Approver eligible yang mencakup Group aset

### Deny pada override dievaluasi sebelum Eligibility
115. `Rina Wijaya {runId}` mengajukan Disposal jenis `Scrap` atas `Truk Terbatas L2 {runId}` dengan scan tag aset
116. Verifikasi pengajuan ditolak oleh Deny pada override aset, yang dievaluasi sebelum Eligibility, walaupun jenis `Scrap` tidak ada di Allowed disposal types `Sell` Category `Kendaraan Terbatas {runId}`
117. Verifikasi tidak ada permintaan approval yang diterima `Budi Santoso {runId}` maupun `Citra Lestari {runId}` untuk aset `Truk Terbatas L2 {runId}`
