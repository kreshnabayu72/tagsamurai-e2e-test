---
id: TC-AC-ACTS-E2E-161-detail-sku-summary-bar-available-dan-banner-waiting-for-approval
title: "Detail SKU: Summary Bar Card Available, Perubahan setelah Delete, dan Banner Waiting for Approval (Jamak, Tunggal, Tidak Tampil, Bukan Collision, Link Review)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-891
  - TC-AC-ACTS-892
  - TC-AC-ACTS-984
  - TC-AC-ACTS-985
  - TC-AC-ACTS-986
  - TC-AC-ACTS-987
  - TC-AC-ACTS-988
coverage:
  web: automated
---

# Detail SKU: Summary Bar Card Available, Perubahan setelah Delete, dan Banner Waiting for Approval (Jamak, Tunggal, Tidak Tampil, Bukan Collision, Link Review)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (#12). Data per blok TC (di-reset fixture BE): 5 Available, 3 Damaged/Missing, 4 In Use (TC-AC-ACTS-891, 892); 2 Subject Register Duplicate pending dari Add Stock (TC-AC-ACTS-984 dan 988; TC-AC-ACTS-988 juga memiliki Subject pending SKU lain); 1 Subject pending (TC-AC-ACTS-985); tanpa Subject pending (TC-AC-ACTS-986); hanya Subject Activation Collision pending dari aktivasi Client (TC-AC-ACTS-987). Hitungan Summary bar dibaca relatif terhadap seeding (S-12).

## Test Steps

### TC-AC-ACTS-891: Summary bar Detail SKU, card Available = jumlah unit berstatus Available

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List
2. Amati Summary bar
3. Verifikasi card berurutan `Total Registered` `12`, `Available` `5`, `In Use` `4`
4. Terapkan Filter Status = Available pada Tab Available
5. Verifikasi jumlah baris berstatus Available pada Tab Available sama dengan card Available (5) dan card Available tidak menghitung unit Damaged/Missing
6. Verifikasi tidak ada card `Allocated` maupun `Damaged/Missing`
7. Kosongkan Filter Status

### TC-AC-ACTS-984: Banner Waiting for Approval dengan hitungan jamak

8. Reset dataset: 2 Subject Register Duplicate pending lewat fixture BE, lalu muat ulang halaman
9. Amati area di atas toolbar Tab Available
10. Verifikasi banner `2 TAGs are waiting for approval.` tampil
11. Verifikasi tabel tidak memuat baris untuk kedua unit itu

### TC-AC-ACTS-988: Approver melihat link Review in Approvals yang membuka Tab Active dengan filter SKU terisi

12. Klik link `Review in Approvals` pada banner
13. Verifikasi halaman `Approvals > TAG Stock` terbuka di Tab Active
14. Verifikasi Filter SKU terisi `RFID-ASSET-CORE-R5`
15. Verifikasi hanya 2 Subject SKU itu tampil
16. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available

### TC-AC-ACTS-985: Banner memakai bentuk tunggal untuk satu unit

17. Reset dataset: 1 Subject Register Duplicate pending lewat fixture BE, lalu muat ulang halaman
18. Amati area di atas toolbar Tab Available
19. Verifikasi banner `1 TAG is waiting for approval.` tampil

### TC-AC-ACTS-986: Banner tidak tampil bila tidak ada unit Register Duplicate yang menunggu

20. Reset dataset: tanpa Subject pending lewat fixture BE, lalu muat ulang halaman
21. Amati area di atas toolbar Tab Available
22. Verifikasi toolbar Tab Available tampil langsung di bawah tab bar
23. Verifikasi tidak ada banner

### TC-AC-ACTS-987: Banner tidak menghitung unit Waiting dari Activation Collision

24. Reset dataset: hanya Subject Activation Collision pending lewat fixture BE, lalu muat ulang halaman
25. Amati area di atas toolbar Tab Available
26. Verifikasi toolbar Tab Available tampil (halaman termuat)
27. Verifikasi tidak ada banner di Tab Available
28. Buka Approvals > TAG Stock > Tab Active
29. Verifikasi Subject Activation Collision hanya terlihat di Tab Active Approvals

### TC-AC-ACTS-892: Card Available berkurang setelah Delete unit Available dan tidak berubah setelah Delete unit Damaged/Missing

30. Reset dataset: 5 Available dan 3 Damaged/Missing lewat fixture BE
31. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
32. Klik (⋯) pada satu unit Available, klik `Delete`, lalu klik `[Delete]`
33. Verifikasi Summary bar card Available `4`
34. Verifikasi Summary bar Total Registered `7`
35. Klik (⋯) pada satu unit Damaged/Missing, klik `Delete`, lalu klik `[Delete]`
36. Verifikasi Summary bar card Available tetap `4`
37. Verifikasi Summary bar Total Registered `6`

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu topik (Detail SKU, satu SKU dan satu dataset); tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah pembukaan Detail SKU dan pemulihan state diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), "Reset dataset", pemulihan Filter Status, navigasi ke Approvals dan kembali ke Detail SKU. Urutan TC: 891, 984, 988, 985, 986, 987, 892; aksi menghapus data (TC-AC-ACTS-892) di akhir spec.
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun dikonfirmasi tim FE.
  - TC-AC-ACTS-891 mengasersi card `Total Registered` `12` dari dataset seeding (5+3+4) dan card Available terhadap jumlah baris berstatus Available; TC tidak menyebut cara menghitung baris (spec memakai Filter Status).
  - TC-AC-ACTS-892 Precondition "5 Available dan 3 Damaged/Missing" mengasersi Total Registered `7` dan `6` pada dataset tanpa unit In Use; angka mengikuti TC dan dataset di-reset sebelum blok.
  - TC-AC-ACTS-988 meminta "Subject pending SKU lain" tanpa menyebut SKU; spec memakai Subject pending seeding pada SKU lain.
