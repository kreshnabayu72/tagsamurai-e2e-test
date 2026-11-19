---
id: TC-FA-ASSIGN-BE-217-pencatatan-log-transaksi
title: "Pencatatan ke log transaksi dan snapshot nama pelaku"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§8.3#b1", "§8.3#b2", "§8.3#b3", "§8.3#b4", "ASSIGN-LOGIC-17a", "ASSIGN-LOGIC-17b", "ASSIGN-LOGIC-17c", "ASSIGN-LOGIC-17d", "ASSIGN-LOGIC-17e", "ASSIGN-LOGIC-17f", "ASSIGN-LOGIC-17g"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§8.3#b1": [4, 12, 15, 18, 20, 52, 55]
  "§8.3#b2": [22, 24, 26, 30, 31]
  "§8.3#b3": 9
  "§8.3#b4": [5, 43, 44, 57, 58]
  "ASSIGN-LOGIC-17a": 6
  "ASSIGN-LOGIC-17b": 7
  "ASSIGN-LOGIC-17c": 4
  "ASSIGN-LOGIC-17d": [33, 37]
  "ASSIGN-LOGIC-17e": [41, 46]
  "ASSIGN-LOGIC-17f": [22, 24, 26, 30]
  "ASSIGN-LOGIC-17g": 41
---

# Pencatatan ke log transaksi dan snapshot nama pelaku

## Prerequisites
- Aktor: Aktor Assignment `Rina Wijaya {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); `Agus Pratama {runId}` (Asset Admin, cakupan Group `Branch Surabaya {runId}`); Group Manager `Tono Wibowo {runId}`; Approver `Hana Permatasari {runId}` dan `Mira Handayani {runId}`; Assignee dan PIC ber-akun login seperti di entri data.
- Data:
  - DU-217-1: User, Aktor Assignment yang kemudian diganti namanya: Nama `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`, Nama sesudah rename `Rina Wijaya Putri {runId}`.
  - DU-217-2: User, Aktor Assignment dengan cakupan satu Group: Nama `Agus Pratama {runId}`, Role `Asset Admin`, Cakupan Group `Branch Surabaya {runId}`.
  - DU-217-3: User, Group Manager sebagai tujuan approval yang dialihkan: Nama `Tono Wibowo {runId}`, Role `Group Manager`, Cakupan Group `Head Office {runId}`.
  - DU-217-4: User, Approver yang kemudian dicabut: Nama `Hana Permatasari {runId}`, Role `Approver`, Cakupan Group `Head Office {runId}`.
  - DU-217-5: User, Approver yang memutuskan: Nama `Mira Handayani {runId}`, Role `Approver`, Cakupan Group `Head Office {runId}`.
  - DU-217-6: Assignment, ASG dengan dua baris Waiting for Handover tanpa konfirmasi penerima: Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop Dell Latitude 5440 {runId}`, Baris 2 `Monitor Samsung 27 {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `No`.
  - DU-217-7: Assignment, ASG Division dengan baris berfield Division aset IT: Assignee `Keuangan {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Brankas Krisbow {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `No`, PIC `Indah Permata {runId}`, Division aset sebelum `IT {runId}`.
  - DU-217-8: Assignment, ASG Employee dengan field Division aset yang tidak berubah: Assignee `Citra Dewi {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Printer Epson L3250 {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `No`, Division aset `IT {runId}`.
  - DU-217-9: Draft, Draft yang dapat dihapus Aktor Group Branch Surabaya: Assignee `Dedi Prasetyo {runId}`, Tipe Assignee `Employee`, Pembuat `Agus Pratama {runId}`, Aset 1 `Kursi Rapat {runId}`, Group aset 1 `Branch Surabaya {runId}`.
  - DU-217-10: Draft, Draft yang dilewati karena memuat aset di luar cakupan Aktor: Assignee `Eko Wijaya {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Meja Rapat {runId}`, Group aset 1 `Head Office {runId}`, Aset 2 `Lemari Besi {runId}`, Group aset 2 `Branch Surabaya {runId}`.
  - DU-217-11: Assignment, ASG dengan baris Waiting for Approval yang approver-nya dicabut: Assignee `Fajar Nugroho {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Speaker Bose {runId}`, Status baris `Waiting for Approval`, Approver `Hana Permatasari {runId}`, Fallback `Tono Wibowo {runId}`.
  - DU-217-12: Assignment, ASG dengan baris Waiting for Handover yang melewati Transaction timeout: Assignee `Gita Lestari {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kamera Nikon D7500 {runId}`, Status baris `Waiting for Handover`.
  - DU-217-13: Assignment, ASG Division yang PIC-nya dinonaktifkan: Assignee `Pemasaran {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Proyektor Hitachi {runId}`, Status baris `Waiting for Handover`, PIC `Novi Andriani {runId}`.
  - DU-217-14: Assignment, ASG dengan sesi konfirmasi yang jendelanya habis: Assignee `Hadi Susanto {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kulkas Sharp {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`.
  - DU-217-15: Assignment, ASG dengan baris Waiting for Approval yang diputuskan lalu dikonfirmasi Assignee: Assignee `Indra Kusuma {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Televisi LG {runId}`, Status baris `Waiting for Approval`, Approver `Mira Handayani {runId}`, Approval Note `Aset dibutuhkan untuk pekerjaan harian`, Pernyataan konfirmasi `I confirm that Indra Kusuma has received these assets and accepted responsibility for them.`.
  - DU-217-16: Assignment, ASG Employee dengan baris Assigned yang Assignee-nya kemudian diganti namanya: Assignee `Joko Susilo {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Mesin Fotokopi Ricoh {runId}`, Status baris `Assigned`, Nama Assignee sesudah rename `Joko Susilo Wibowo {runId}`.
  - DU-217-17: Assignment, ASG Division dengan baris Assigned yang Division-nya kemudian diganti namanya: Assignee `Logistik {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Forklift Toyota {runId}`, Status baris `Assigned`, PIC `Rudi Hartono {runId}`, Nama Division sesudah rename `Logistik Pusat {runId}`, Nama PIC sesudah rename `Rudi Hartono Saputra {runId}`.
  - DU-217-18: Assignment, ASG dengan baris Waiting for Handover yang tag-nya tidak terbaca: Assignee `Kiki Amelia {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Router Cisco {runId}`, Status baris `Waiting for Handover`, Tag baris 1 `tag tidak terbaca`.
  - DU-217-20: Assignment, ASG Division dengan Division aset yang diedit selama Assigned: Assignee `Gudang {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Rak Besi Lion {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `No`, PIC `Taufik Hidayat {runId}`, Division aset sebelum `Umum {runId}`, Division aset hasil edit `Teknik {runId}`.
  - DU-217-21: Assignment, ASG Division dengan dua aset: Assignee `Pemasaran {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Layar Proyektor Screenpro {runId}`, Baris 2 `Kamera Canon M50 {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `No`, PIC `Umar Hakim {runId}`, Division aset sebelum `IT {runId}`.
  - DU-217-22: Assignment, ASG Employee dengan baris Assigned yang tag-nya tidak terbaca saat Unassign: Assignee `Lutfi Hakim {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Scanner Fujitsu fi-7160 {runId}`, Status baris `Assigned`, Tag baris 1 `tag tidak terbaca`.
- Kondisi:
  - Transaction timeout memakai nilai yang berlaku untuk entitas aktor dan tidak diubah spec ini.
  - Jendela konfirmasi Handover bernilai `15 menit`.

## Test Steps

### Handover tidak menulis ke log sistem dan terbaca di tiga tampilan log transaksi
1. Rina mencatat jumlah entri `Changelog`, `System Log`, `Activity Log`, dan `TAG Log` sebelum aksi
2. Rina memverifikasi tag baris `Laptop Dell Latitude 5440 {runId}` dan `Monitor Samsung 27 {runId}` pada DU-217-6
3. Rina menekan `[Complete Handover]` untuk kedua baris
4. Verifikasi jumlah entri `Changelog`, `System Log`, dan `Activity Log` tidak bertambah oleh transaksi Assignment
5. Verifikasi jumlah entri `TAG Log` tidak bertambah karena Assignment tidak mengubah status TAG
6. Verifikasi peristiwa Handover dicatat sekali ke log transaksi dan terbaca di Assignment Log, Transaction log aset, dan Transaction admin log
7. Verifikasi User log Assignee `Budi Santoso {runId}` memuat peristiwa Handover itu

### Download tidak dicatat
8. Rina melakukan Download daftar ASG
9. Verifikasi Download tidak dicatat di log mana pun

### Perubahan field Division aset dicatat di Changelog Asset
10. Rina memverifikasi tag baris `Brankas Krisbow {runId}` pada DU-217-7
11. Rina menekan `[Complete Handover]` untuk baris `Brankas Krisbow {runId}`
12. Verifikasi `Changelog` Asset memuat satu entri untuk `Brankas Krisbow {runId}` dengan Field `Division`, Old `IT {runId}`, dan New `Keuangan {runId}`
13. Rina memverifikasi tag baris `Brankas Krisbow {runId}` untuk Unassign
14. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Keuangan {runId}`
15. Verifikasi `Changelog` Asset memuat entri berikutnya dengan Field `Division`, Old `Keuangan {runId}`, dan New `IT {runId}` dari nilai snapshot
16. Rina memverifikasi tag baris `Printer Epson L3250 {runId}` pada DU-217-8
17. Rina menekan `[Complete Handover]` untuk baris `Printer Epson L3250 {runId}`
18. Verifikasi `Changelog` Asset tidak memuat entri baru untuk `Printer Epson L3250 {runId}` karena field `Division` tidak berubah pada Assignee Employee

### Bulk Delete Draft dengan item dilewati
19. Agus menghapus Draft `Dedi Prasetyo {runId}` pada DU-217-9 dan Draft `Eko Wijaya {runId}` pada DU-217-10 sekaligus
20. Verifikasi hanya Draft `Dedi Prasetyo {runId}` yang terhapus dan tercatat, sedangkan Draft `Eko Wijaya {runId}` yang dilewati tidak dicatat

### Peristiwa otomatis dicatat dengan pelaku System
21. Approver `Hana Permatasari {runId}` pada DU-217-11 dicabut saat baris `Speaker Bose {runId}` menunggu
22. Verifikasi node `Approval rerouted` pada baris `Speaker Bose {runId}` memuat pelaku `System` dan baris detail `Routed to: Group Manager (no eligible approver)`
23. Waktu berlalu sampai baris `Kamera Nikon D7500 {runId}` pada DU-217-12 melewati Transaction timeout sejak masuk `Waiting for Handover`
24. Verifikasi node `Canceled by [Actor]` pada baris `Kamera Nikon D7500 {runId}` memuat pelaku `System`
25. PIC `Novi Andriani {runId}` pada DU-217-13 dinonaktifkan
26. Verifikasi node `PIC changed by [Actor]` untuk baris `Proyektor Hitachi {runId}` memuat pelaku `System` karena baris menjadi `No PIC`
27. Rina memverifikasi tag baris `Kulkas Sharp {runId}` pada DU-217-14
28. Rina menekan `[Request Confirmation]`
29. Waktu berlalu sampai `15 menit` sejak `[Request Confirmation]` tanpa konfirmasi
30. Verifikasi node `Confirmation not received` pada baris `Kulkas Sharp {runId}` memuat pelaku `System`
31. Verifikasi peristiwa otomatis di atas juga tercatat di User log Assignee dengan pelaku `System`

### Keputusan approver dan konfirmasi Assignee dicatat per aset
32. Mira menyetujui baris `Televisi LG {runId}` pada DU-217-15 dengan Approval Note `Aset dibutuhkan untuk pekerjaan harian`
33. Verifikasi node `Approved by [Approver]` pada baris `Televisi LG {runId}` memuat pelaku `Mira Handayani {runId}`, waktu keputusan, dan Note `Aset dibutuhkan untuk pekerjaan harian`
34. Rina memverifikasi tag baris `Televisi LG {runId}`
35. Rina menekan `[Request Confirmation]` untuk baris `Televisi LG {runId}`
36. Assignee `Indra Kusuma {runId}` mengonfirmasi penerimaan dengan pernyataan `I confirm that Indra Kusuma has received these assets and accepted responsibility for them.` dicentang
37. Verifikasi node `Handed over` pada baris `Televisi LG {runId}` memuat cara konfirmasi, waktu, pelaku, dan teks pernyataan yang dicentang

### Rename di master data tidak mengubah log
38. Nama Aktor `Rina Wijaya {runId}` diganti menjadi `Rina Wijaya Putri {runId}`
39. Nama Assignee `Joko Susilo {runId}` pada DU-217-16 diganti menjadi `Joko Susilo Wibowo {runId}`
40. Nama Assignee `Logistik {runId}` bertipe `Division` pada DU-217-17 diganti menjadi `Logistik Pusat {runId}`
41. Verifikasi log lama memuat nama pelaku `Rina Wijaya {runId}`, Assignee `Joko Susilo {runId}`, dan Assignee `Logistik {runId}` bertipe `Division` sebagai nilai saat peristiwa terjadi

### Report TAG dicatat oleh pemilik TAG Log
42. Rina melaporkan tag aset `Router Cisco {runId}` pada DU-217-18 tidak terbaca lewat `I Can't Scan the TAG` saat Handover
43. Verifikasi Assignment Log baris `Router Cisco {runId}` memuat node `TAG reported by [Reporter]`
44. Verifikasi `TAG Log` memuat entri Report TAG yang dicatat oleh pemilik TAG Log, bukan oleh Assignment

### Nama PIC di log adalah nilai saat peristiwa terjadi
45. Nama PIC `Rudi Hartono {runId}` pada DU-217-17 diganti menjadi `Rudi Hartono Saputra {runId}`
46. Verifikasi log lama baris `Forklift Toyota {runId}` memuat PIC `Rudi Hartono {runId}` sebagai nilai saat peristiwa terjadi

### Nilai Division hasil edit dipertahankan saat Unassign
47. Rina memverifikasi tag baris `Rak Besi Lion {runId}` pada DU-217-20
48. Rina menekan `[Complete Handover]` untuk baris `Rak Besi Lion {runId}`
49. Rina mengubah field `Division` aset `Rak Besi Lion {runId}` menjadi `Teknik {runId}` selama baris `Assigned`
50. Rina memverifikasi tag baris `Rak Besi Lion {runId}` untuk Unassign
51. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Gudang {runId}`
52. Verifikasi jumlah entri `Changelog` Asset untuk `Rak Besi Lion {runId}` tidak bertambah oleh Unassign dan field `Division` tetap `Teknik {runId}`

### Satu entri Changelog Asset per aset pada ASG Division berisi beberapa aset
53. Rina memverifikasi tag baris `Layar Proyektor Screenpro {runId}` dan `Kamera Canon M50 {runId}` pada DU-217-21
54. Rina menekan `[Complete Handover]` untuk kedua baris
55. Verifikasi `Changelog` Asset memuat satu entri terpisah untuk `Layar Proyektor Screenpro {runId}` dan satu entri untuk `Kamera Canon M50 {runId}`, masing-masing dengan Field `Division`, Old `IT {runId}`, dan New `Pemasaran {runId}`

### Report TAG saat Unassign dicatat oleh pemilik TAG Log
56. Rina melaporkan tag aset `Scanner Fujitsu fi-7160 {runId}` pada DU-217-22 tidak terbaca lewat `I Can't Scan the TAG` saat Unassign
57. Verifikasi Assignment Log baris `Scanner Fujitsu fi-7160 {runId}` memuat node `TAG reported by [Reporter]`
58. Verifikasi `TAG Log` memuat entri Report TAG yang dicatat oleh pemilik TAG Log, bukan oleh Assignment
