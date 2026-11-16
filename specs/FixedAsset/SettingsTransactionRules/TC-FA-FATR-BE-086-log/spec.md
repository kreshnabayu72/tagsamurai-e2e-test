---
id: TC-FA-FATR-BE-086-log
title: "Isi entri Changelog"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["§8.1#r2", "§9.2#b42", "§9.2#b55", "§9.2#p17", "§9.2#b377", "§9.4.2#r5", "§9.4.2#r6", "§9.4.2#r32", "§9.4.2#r84", "§9.4.3#b8", "§9.4.4#r5", "§9.4.4#r14", "§9.4.4#r34", "§9.4.4#r45", "§9.6#r1", "§9.6#r9", "§9.7#r9", "§9.8#r13", "§9.8#r14", "§9.8#r15", "§9.10.1#b9", "§9.10.2#b7", "§9.10.3#b7"]
smoke: []
dependsOn: []
trace:
  "§8.1#r2": 6
  "§9.2#b42": 10
  "§9.2#b55": 18
  "§9.2#p17": [4, 5]
  "§9.2#b377": [22, 24]
  "§9.4.2#r5": [18, 19]
  "§9.4.2#r6": 14
  "§9.4.2#r32": 29
  "§9.4.2#r84": 3
  "§9.4.3#b8": [18, 22, 24]
  "§9.4.4#r5": 15
  "§9.4.4#r14": 18
  "§9.4.4#r34": [36, 38, 39]
  "§9.4.4#r45": [22, 24]
  "§9.6#r1": 3
  "§9.6#r9": 18
  "§9.7#r9": 3
  "§9.8#r13": [18, 19]
  "§9.8#r14": [22, 24]
  "§9.8#r15": 40
  "§9.10.1#b9": 40
  "§9.10.2#b7": 40
  "§9.10.3#b7": 40
---
# Isi entri Changelog

## Prerequisites
- Aktor: Maya Pengelola (DU-086-1) dan Budi Penyunting (DU-086-2), keduanya Total Control dengan cakupan seluruh Group.
- Data:
  - DU-086-1: User, pengelola yang menyimpan setting dan override: Name `Maya Pengelola {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-086-2: User, pengelola kedua yang menyimpan dan menghapus lebih dulu: Name `Budi Penyunting {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-086-4: Category, Category leaf untuk entri Changelog per field: Name `Perangkat Log {runId}`.
  - DU-086-5: Category, Category leaf untuk perubahan Inherit ke nilai sendiri: Name `Peralatan Log {runId}`.
  - DU-086-6: Category, Category leaf untuk guard Allowed assignee: Name `Alat Ukur Log {runId}`.
  - DU-086-7: Group, Group target override yang dibuat lalu dihapus: Name `Tim Log {runId}`.
  - DU-086-8: Group, Group target override yang dihapus dua kali: Name `Tim Log Dua {runId}`.
  - DU-086-9: Group, Group target override yang ditolak guard: Name `Tim Log Tiga {runId}`.
  - DU-086-10: Group, Group target override yang boleh dihapus: Name `Tim Log Empat {runId}`.
  - DU-086-11: Asset, aset target override Asset pada guard Allowed assignee: Name `Alat Ukur Tiga {runId}`; Asset Name `Alat Ukur Lapangan {runId}`; Category `Alat Ukur Log {runId}`; Group `Tim Log Tiga {runId}`.
- Kondisi:
  - Seluruh field Category `Perangkat Log {runId}`, `Peralatan Log {runId}`, dan `Alat Ukur Log {runId}` bernilai Inherit, dan belum ada override pada ketiga Category itu.
  - Max duration Category `Perangkat Log {runId}` belum bernilai sendiri sebelum Save pertama di spec ini.
  - Allowed assignee: Employee `ON` dan Allowed assignee: Division `ON` pada Company default.
  - Allow Assign bernilai `Allow` pada Company default dan Inherit pada Category `Alat Ukur Log {runId}`; spec ini tidak mengubahnya, sehingga penolakan guard Allowed assignee berlaku untuk aset yang nilai efektif Allow Assign-nya bukan Deny.
  - Entri Changelog dibaca per Category `{runId}` milik spec ini; kolom Field memuat nama transaksi diikuti nama field dalam kurung.

## Test Steps

### Save yang mengubah dua field menulis satu entri Changelog per field
1. Maya Pengelola mencatat jumlah entri Changelog untuk Category `Perangkat Log {runId}`
2. Maya Pengelola menyimpan Category `Perangkat Log {runId}` dengan Max duration nilai sendiri `16` hari dan Photo at start nilai sendiri `OFF` dalam satu Save
3. Verifikasi Changelog untuk Category `Perangkat Log {runId}` bertambah tepat dua entri, satu per field yang berubah
4. Verifikasi entri Max duration memuat Category `Perangkat Log {runId}`, kolom Field memuat nama transaksi dan nama field `Max duration`, Old Value `Inherit`, New Value `16 days`, dan pelaku `Maya Pengelola {runId}`
5. Verifikasi entri Photo at start memuat Category `Perangkat Log {runId}`, kolom Field memuat nama transaksi dan nama field `Photo at start`, Old Value `Inherit`, New Value `OFF`, dan pelaku `Maya Pengelola {runId}`
6. Verifikasi kedua entri memiliki object path `Transaction Settings`

### Old Value adalah nilai tersimpan saat Save diterima
7. Maya Pengelola membaca Max duration Category `Perangkat Log {runId}` yang tersimpan `16`
8. Budi Penyunting menyimpan Category `Perangkat Log {runId}` dengan Max duration nilai sendiri `18`
9. Maya Pengelola mengirim Save Category `Perangkat Log {runId}` dengan Max duration `20`, berdasarkan nilai `16` yang dibacanya lebih dulu
10. Verifikasi entri Changelog terbaru untuk Max duration Category `Perangkat Log {runId}` memuat Old Value `18 days` dan New Value `20 days`, nilai tersimpan saat Save diterima, bukan nilai yang dibaca Maya Pengelola

### Inherit diganti nilai sendiri dengan angka yang sama dicatat sebagai perubahan field biasa
11. Maya Pengelola mencatat jumlah entri Changelog untuk Category `Peralatan Log {runId}`
12. Maya Pengelola membaca nilai Company default Max extensions yang berlaku
13. Maya Pengelola menyimpan Category `Peralatan Log {runId}` dengan Max extensions nilai sendiri yang angkanya sama dengan nilai Company default Max extensions yang dibacanya pada langkah sebelumnya
14. Verifikasi Changelog untuk Category `Peralatan Log {runId}` bertambah tepat satu entri dengan Old Value `Inherit`, sehingga perpindahan itu dicatat sebagai perubahan
15. Verifikasi entri itu adalah entri perubahan field biasa dengan Action `Edit`, bukan entri berstatus

### Save tanpa selisih tidak menulis entri log
16. Maya Pengelola mencatat jumlah entri Changelog untuk Category `Perangkat Log {runId}` dan System Log milik Maya Pengelola
17. Maya Pengelola mengirim ulang Save Category `Perangkat Log {runId}` dengan Max duration `20`, nilai yang sudah tersimpan
18. Verifikasi Changelog untuk Category `Perangkat Log {runId}` tidak bertambah entri
19. Verifikasi System Log milik Maya Pengelola tidak bertambah entri

### Add override dan Delete override tidak masuk Changelog
20. Maya Pengelola mencatat jumlah entri Changelog untuk Category `Perangkat Log {runId}`
21. Maya Pengelola menambahkan override Group `Tim Log {runId}` pada Category `Perangkat Log {runId}` untuk transaksi peminjaman dengan Max duration `5`
22. Verifikasi Changelog untuk Category `Perangkat Log {runId}` tidak bertambah entri karena pembuatan override tidak masuk Changelog
23. Maya Pengelola menghapus override Group `Tim Log {runId}` pada Category `Perangkat Log {runId}` untuk transaksi peminjaman
24. Verifikasi Changelog untuk Category `Perangkat Log {runId}` tetap tidak bertambah entri karena penghapusan override tidak masuk Changelog

### Override yang sudah dihapus pengguna lain dihapus lagi tanpa efek ganda dan tanpa log tambahan
25. Maya Pengelola menambahkan override Group `Tim Log Dua {runId}` pada Category `Perangkat Log {runId}` untuk transaksi peminjaman dengan Max duration `6`
26. Budi Penyunting menghapus override Group `Tim Log Dua {runId}` pada Category `Perangkat Log {runId}`
27. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log untuk Category `Perangkat Log {runId}`
28. Maya Pengelola menghapus override Group `Tim Log Dua {runId}` yang sama, yang sudah dihapus Budi Penyunting
29. Verifikasi override Group `Tim Log Dua {runId}` tidak ada tanpa efek ganda, dan Changelog serta Activity Log untuk Category `Perangkat Log {runId}` tidak bertambah entri

### Delete yang ditolak guard tidak menulis log dan bulk campuran hanya mencatat override yang terhapus
30. Maya Pengelola menyimpan Category `Alat Ukur Log {runId}` dengan Allowed assignee: Division nilai sendiri `OFF` lewat Save Changes
31. Maya Pengelola menambahkan override Group `Tim Log Tiga {runId}` pada Category `Alat Ukur Log {runId}` untuk transaksi penugasan dengan Allowed assignee: Division `ON`
32. Maya Pengelola menambahkan override aset `Alat Ukur Tiga {runId}` pada Category `Alat Ukur Log {runId}` untuk transaksi penugasan dengan Allowed assignee: Employee `OFF`
33. Maya Pengelola menambahkan override Group `Tim Log Empat {runId}` pada Category `Alat Ukur Log {runId}` untuk transaksi penugasan dengan Max assets per assignee (concurrent) `2`
34. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log untuk Category `Alat Ukur Log {runId}`
35. Maya Pengelola menghapus override Group `Tim Log Tiga {runId}`, yang akan membuat kombinasi efektif Allowed assignee: Employee dan Allowed assignee: Division override aset `Alat Ukur Tiga {runId}` sama-sama `OFF`
36. Verifikasi Delete ditolak, override Group `Tim Log Tiga {runId}` masih ada, dan Changelog serta Activity Log untuk Category `Alat Ukur Log {runId}` tidak bertambah entri
37. Maya Pengelola menghapus bulk override Group `Tim Log Tiga {runId}` dan override Group `Tim Log Empat {runId}`
38. Verifikasi override Group `Tim Log Empat {runId}` terhapus dan override Group `Tim Log Tiga {runId}` dilewati karena ditolak guard
39. Verifikasi Activity Log untuk Category `Alat Ukur Log {runId}` bertambah tepat satu entri, untuk override Group `Tim Log Empat {runId}` yang terhapus, dan Changelog tidak bertambah entri

### Changelog halaman ini hanya memuat perubahan field Settings
40. Verifikasi seluruh entri Changelog untuk Category `Perangkat Log {runId}` adalah entri perubahan field Settings dengan object path `Transaction Settings`, dan tidak ada entri perubahan toggle atau level plan karena perubahan itu bukan perubahan Settings dan tidak dicatat di halaman ini
