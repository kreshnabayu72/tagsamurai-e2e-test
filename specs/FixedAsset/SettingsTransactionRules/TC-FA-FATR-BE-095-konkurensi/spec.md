---
id: TC-FA-FATR-BE-095-konkurensi
title: "Konkurensi dan aksi berulang pada Settings dan override"
layer: be-e2e
priority: Critical
caseType: Negative
status: draft
owner: BE
sourceRules: ["§9.2#b39", "§9.2#b65", "§9.2#b180", "§9.4.2#r32", "§9.4.2#r88", "§9.4.2#r90", "§9.4.4#r17", "§9.4.4#r32", "§9.6#r3", "§9.6#r18", "§9.6#r19", EB-ERR-3, EB-CON-1, EB-CON-2, EB-CON-3, EB-EDG-1]
smoke: []
dependsOn: []
trace:
  "§9.2#b39": [13, 14]
  "§9.2#b65": 7
  "§9.2#b180": [28, 29]
  "§9.4.2#r32": [30, 31, 32]
  "§9.4.2#r88": 7
  "§9.4.2#r90": 8
  "§9.4.4#r17": 8
  "§9.4.4#r32": [30, 31]
  "§9.6#r3": [29, 30]
  "§9.6#r18": [17, 18]
  "§9.6#r19": 7
  EB-ERR-3: [28, 29, 30, 31]
  EB-CON-1: [6, 7]
  EB-CON-2: [21, 22, 23]
  EB-CON-3: [21, 34, 35]
  EB-EDG-1: 29
---
# Konkurensi dan aksi berulang pada Settings dan override

## Prerequisites
- Aktor: Maya Pengelola (DU-095-1) dan Budi Penyunting (DU-095-2), keduanya Total Control dengan cakupan seluruh Group.
- Data:
  - DU-095-1: User, pengelola pertama yang menyimpan dan mengelola override: Name `Maya Pengelola {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-095-2: User, pengelola kedua yang bertindak bersamaan dengan pengelola pertama: Name `Budi Penyunting {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-095-3: Category, Category leaf yang mewarisi seluruh nilai: Name `Perangkat Serentak {runId}`.
  - DU-095-4: Group, Group target Add override serentak: Name `Tim Serentak {runId}`.
  - DU-095-5: Group, Group target override yang dihapus dua kali: Name `Tim Hapus Serentak {runId}`.
  - DU-095-6: Group, Group target override yang dihapus bersamaan dengan Save Category: Name `Tim Pasangan {runId}`.
  - DU-095-7: Override, override yang dihapus Budi Penyunting lalu dihapus lagi Maya Pengelola: Scope `Group`; Target `Tim Hapus Serentak {runId}`; Category `Perangkat Serentak {runId}`; Transaksi `peminjaman`; Field `Max duration`; Value `5`.
  - DU-095-8: Override, override yang dihapus bersamaan dengan Save Category: Scope `Group`; Target `Tim Pasangan {runId}`; Category `Perangkat Serentak {runId}`; Transaksi `peminjaman`; Field `Max duration`; Value `5`.
  - DU-095-9 sampai DU-095-15 adalah nilai input Save dan Add override di langkah masing-masing, bukan record yang sudah ada.
- Kondisi:
  - Seluruh field Category `Perangkat Serentak {runId}` bernilai Inherit dan belum ada override pada Category itu selain DU-095-7 dan DU-095-8.
  - Jumlah entri Changelog dan Activity Log serta versi setting dibaca sebagai selisih terhadap nilai yang dicatat sebelum aksi, karena pihak lain dapat mengubahnya.
  - Pembukaan draft oleh kedua pengelola terjadi sebelum Save pertama diterima, sehingga keduanya memulai dari nilai tersimpan yang sama.

## Test Steps

### Dua pengelola menyimpan field yang sama: Save terakhir yang diterima server menimpa
1. Maya Pengelola mencatat jumlah entri Changelog
2. Maya Pengelola mengisi draft Category `Perangkat Serentak {runId}` dengan Max duration nilai sendiri `15` tanpa menyimpan
3. Budi Penyunting mengisi draft Category `Perangkat Serentak {runId}` dengan Max duration nilai sendiri `25` tanpa menyimpan
4. Maya Pengelola menyimpan draft-nya
5. Budi Penyunting menyimpan draft-nya setelah Save Maya Pengelola diterima server
6. Verifikasi kedua Save diterima tanpa dialog konflik
7. Verifikasi Max duration Category `Perangkat Serentak {runId}` bernilai `25`, karena Save terakhir yang diterima server menimpa
8. Verifikasi Changelog bertambah tepat dua entri untuk Max duration dari catatan awal, satu per Save, dan entri Maya Pengelola tidak digabung dengan entri Budi Penyunting

### Field yang tidak disentuh draft tidak ditimpa oleh Save yang lebih lambat
9. Maya Pengelola mengisi draft Category `Perangkat Serentak {runId}` dengan Max duration nilai sendiri `20` tanpa menyimpan
10. Budi Penyunting mengisi draft Category `Perangkat Serentak {runId}` dengan Max extensions nilai sendiri `2` tanpa menyimpan
11. Budi Penyunting menyimpan draft-nya
12. Maya Pengelola menyimpan draft-nya setelah Save Budi Penyunting diterima server
13. Verifikasi Max duration Category `Perangkat Serentak {runId}` bernilai `20`
14. Verifikasi Max extensions Category `Perangkat Serentak {runId}` tetap `2`, karena field yang tidak disentuh draft Maya Pengelola tidak ditulis dan perubahan Budi Penyunting tidak tertimpa

### Save yang sama terkirim dua kali berturut-turut tidak menggandakan efek
15. Maya Pengelola mencatat jumlah entri Changelog dan versi setting
16. Maya Pengelola mengirim Save Category `Perangkat Serentak {runId}` dengan Max duration `30` dua kali berturut-turut tanpa jeda
17. Verifikasi Max duration Category `Perangkat Serentak {runId}` bernilai `30`
18. Verifikasi Changelog bertambah tepat satu entri Max duration dan versi setting naik tepat satu dari yang dicatat, karena pengiriman ganda tidak menggandakan efek

### Dua pengelola menambahkan override pada target yang sama bersamaan
19. Maya Pengelola mencatat jumlah override Category `Perangkat Serentak {runId}`
20. Maya Pengelola dan Budi Penyunting menambahkan bersamaan override Group `Tim Serentak {runId}` pada Category `Perangkat Serentak {runId}` untuk transaksi peminjaman, Maya Pengelola dengan Max duration `5` dan Budi Penyunting dengan Max duration `6`
21. Verifikasi tepat satu dari kedua Add override diterima
22. Verifikasi Add override yang lain ditolak dengan pesan `An active override already exists for this target, category, and transaction. Delete it first`
23. Verifikasi jumlah override Category `Perangkat Serentak {runId}` bertambah tepat satu dari yang dicatat, dengan satu override aktif untuk Group `Tim Serentak {runId}`

### Override yang sudah dihapus pengelola lain dihapus lagi tanpa efek ganda
24. Maya Pengelola dan Budi Penyunting membuka daftar override Category `Perangkat Serentak {runId}` yang memuat override Group `Tim Hapus Serentak {runId}`
25. Maya Pengelola mencatat jumlah entri Activity Log dan versi setting
26. Budi Penyunting menghapus override Group `Tim Hapus Serentak {runId}`
27. Maya Pengelola menghapus override Group `Tim Hapus Serentak {runId}` dari daftarnya yang belum diperbarui
28. Verifikasi override Group `Tim Hapus Serentak {runId}` sudah terhapus
29. Verifikasi tidak ada override lain yang ikut terhapus oleh Delete kedua
30. Verifikasi Activity Log bertambah tepat satu entri Delete override, bukan dua, karena tidak ada entri bila tidak ada override terhapus
31. Verifikasi versi setting naik tepat satu dari yang dicatat, karena Delete kedua tidak menambah efek
32. Verifikasi baris override Group `Tim Hapus Serentak {runId}` hilang dari daftar setelah daftar diperbarui

### Save Category dan Delete override pada record berbeda bersamaan sama-sama berhasil
33. Maya Pengelola dan Budi Penyunting bertindak bersamaan: Maya Pengelola menyimpan Category `Perangkat Serentak {runId}` dengan Max duration nilai sendiri `35`, dan Budi Penyunting menghapus override Group `Tim Pasangan {runId}`
34. Verifikasi Save Maya Pengelola diterima dan Max duration Category `Perangkat Serentak {runId}` bernilai `35`
35. Verifikasi Delete Budi Penyunting diterima dan override Group `Tim Pasangan {runId}` terhapus
