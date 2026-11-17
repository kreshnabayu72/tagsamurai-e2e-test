---
id: TC-FA-FATR-BE-093-changelog-berkas
title: "Isi berkas unduhan Changelog"
layer: be-e2e
priority: High
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["EB-DL-4", "EB-DL-5", "EB-DL-1@changelog", "§9.2#b355"]
smoke: []
dependsOn: []
trace:
  "EB-DL-4": [4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 23]
  "EB-DL-5": [27, 28, 29]
  "EB-DL-1@changelog": 6
  "§9.2#b355": 12
---
# Isi berkas unduhan Changelog

## Prerequisites
- Aktor: Maya Pengelola (DU-093-2), Total Control dengan cakupan seluruh Group.
- Data:
  - DU-093-1: Entitas, entitas khusus spec ini dengan Changelog yang sudah terisi: Name `Entitas Unduh Log {runId}`.
  - DU-093-2: User, pengelola Total Control yang mengunduh Changelog: Name `Maya Pengelola {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-093-3: User, pengubah lama yang sudah dinonaktifkan: Name `Budi Lama {runId}`; Status `Inactive`.
  - DU-093-4: Category, Category leaf yang muncul pada entri Changelog terunduh: Name `Perangkat Unduh {runId}`.
  - DU-093-5: Changelog, entri Max duration tertua pada Category Perangkat Unduh: Action `Edit`; Category `Perangkat Unduh {runId}`; Field `Borrow (Max duration)`; Old Value `Inherit`; New Value `16 days`; Modified By `Maya Pengelola {runId}`.
  - DU-093-6: Changelog, entri Max extensions 0 pada Category Perangkat Unduh, dari pengubah yang sudah dinonaktifkan: Action `Edit`; Category `Perangkat Unduh {runId}`; Field `Borrow (Max extensions)`; Old Value `Inherit`; New Value `No extension`; Modified By `Budi Lama {runId}`.
  - DU-093-7: Changelog, entri nilai berderet Allowed disposal types pada Category Perangkat Unduh: Action `Edit`; Category `Perangkat Unduh {runId}`; Field `Disposal (Allowed disposal types)`; Old Value `Sell, Scrap, Write-off`; New Value `Sell, Scrap`; Modified By `Maya Pengelola {runId}`.
  - DU-093-8: Changelog, entri Damaged & Missing pada All categories: Action `Edit`; Category `All categories`; Field `Damaged & Missing (Long missing after)`; Old Value `30 days`; New Value `Off`; Modified By `Maya Pengelola {runId}`.
  - DU-093-9: Changelog, entri massal berantai dari `10 days` ke `11 days` pada Category Berkas Massal (2550 record): Action `Edit`; Category `Berkas Massal {runId}`; Field `Borrow (Max duration)`; Old Value `10 days`; New Value `11 days`; Modified By `Maya Pengelola {runId}`; Date `T0 − {n} menit`.
  - DU-093-10: Category, Category leaf yang muncul pada entri massal Changelog: Name `Berkas Massal {runId}`.
  - DU-093-11: Changelog, entri pertama Max duration pada Category Berkas Massal, satu-satunya yang ber-Old Value `Inherit`: Action `Edit`; Category `Berkas Massal {runId}`; Field `Borrow (Max duration)`; Old Value `Inherit`; New Value `10 days`; Modified By `Maya Pengelola {runId}`.
  - DU-093-12: Changelog, entri massal berantai dari `11 days` kembali ke `10 days` pada Category Berkas Massal (2549 record): Action `Edit`; Category `Berkas Massal {runId}`; Field `Borrow (Max duration)`; Old Value `11 days`; New Value `10 days`; Modified By `Maya Pengelola {runId}`; Date `T0 − {n} menit`.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Unduh Log {runId}` (DU-093-1) yang tidak dipakai spec lain, karena Changelog diisi data awal bervolume besar.
  - Changelog entitas memuat entri DU-093-5 sampai DU-093-9, DU-093-11, dan DU-093-12, yang bersama-sama berjumlah 5.104 entri, di atas 5.000.
  - Entri Category `Berkas Massal {runId}` berantai menurut urutan Date: DU-093-11 lebih dulu, lalu DU-093-9 dan DU-093-12 bergantian, sehingga Old Value setiap entri sama dengan New Value entri sebelumnya pada Category dan Field yang sama, dan hanya entri pertama yang ber-Old Value `Inherit`.
  - Entri DU-093-5 sampai DU-093-8 dicatat berurutan dari yang tertua ke yang terbaru, semuanya sesudah seluruh entri Category `Berkas Massal {runId}`.
  - Date Format `dd/MM/yy` pada General Settings, dan seluruh kolom Changelog tampil.
  - Berkas diunduh dengan nama `Changelog-Transaction-Settings`.

## Test Steps

### Unduhan CSV: encoding, header, dan urutan baris mengikuti sort aktif
1. Maya Pengelola membuka Changelog dan menyaring Category `Perangkat Unduh {runId}`
2. Maya Pengelola mengurutkan kolom Date dari Oldest First
3. Maya Pengelola mengunduh hasilnya sebagai CSV
4. Verifikasi berkas CSV berencoding UTF-8 dengan BOM
5. Verifikasi baris header berkas berisi `Date`, `Action`, `Category`, `Field`, `Old Value`, `New Value`, dan `Modified By`
6. Verifikasi berkas memuat tepat tiga baris data, hanya untuk Category `Perangkat Unduh {runId}`
7. Verifikasi baris data berurutan menurut sort aktif dari entri tertua: Field `Borrow (Max duration)`, `Borrow (Max extensions)`, lalu `Disposal (Allowed disposal types)`
8. Maya Pengelola mengurutkan kolom Date dari Newest First
9. Maya Pengelola mengunduh hasilnya sebagai CSV
10. Verifikasi baris data berurutan menurut sort aktif dari entri terbaru: Field `Disposal (Allowed disposal types)`, `Borrow (Max extensions)`, lalu `Borrow (Max duration)`

### Isi sel per tipe kolom Changelog
11. Verifikasi sel Old Value dan New Value baris Max duration ditulis `Inherit` dan `16 days`
12. Verifikasi sel New Value baris Max extensions ditulis `No extension`, karena Changelog menulis nilai 0 sebagai teks maknanya
13. Verifikasi sel Modified By baris Max extensions ditulis `Budi Lama {runId}`, nama pengubah yang sudah dinonaktifkan
14. Verifikasi sel Old Value baris Allowed disposal types ditulis `Sell, Scrap, Write-off` dan sel New Value ditulis `Sell, Scrap`, dengan nilai berderet dipisah `", "`
15. Verifikasi sel Field baris entri All categories ditulis `Damaged & Missing (Long missing after)`
16. Verifikasi tidak ada sel yang kosong pada baris data, karena Changelog tidak pernah memiliki nilai kosong
17. Verifikasi berkas tidak memuat kolom foto

### Unduhan XLSX: satu sheet bernama Sheet1
18. Maya Pengelola mengunduh hasil yang sama sebagai XLSX
19. Verifikasi berkas XLSX memuat satu sheet bernama `Sheet1`
20. Verifikasi sheet `Sheet1` memuat baris header yang sama dengan CSV dan tiga baris data dalam urutan sort aktif

### Nol baris menghasilkan berkas berisi header saja
21. Maya Pengelola mencari `Tidak Ada {runId}` di Changelog
22. Maya Pengelola mengunduh hasilnya sebagai CSV
23. Verifikasi berkas CSV hanya memuat baris header tanpa baris data

### Lebih dari 5.000 baris: berkas memuat seluruh baris
24. Maya Pengelola menghapus pencarian dan saringan di Changelog
25. Maya Pengelola mencatat jumlah entri Changelog entitas
26. Maya Pengelola mengunduh seluruh Changelog sebagai CSV
27. Verifikasi berkas terunduh langsung dari satu permintaan, tanpa job background dan tanpa notifikasi
28. Verifikasi jumlah baris data berkas sama dengan jumlah entri Changelog yang dicatat, lebih dari 5.000
29. Verifikasi baris data berkas memuat entri Category `Berkas Massal {runId}` dan entri Category `Perangkat Unduh {runId}`
