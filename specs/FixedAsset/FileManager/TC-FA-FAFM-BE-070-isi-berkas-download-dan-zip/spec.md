---
id: TC-FA-FAFM-BE-070-isi-berkas-download-dan-zip
title: "Isi berkas Download tabel dan ZIP"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["ACT-03j", "ACT-03k", "EB-DL-4", "EB-DL-5"]
smoke: []
dependsOn: []
trace:
  "ACT-03j": [23, 24, 25, 46, 47, 48]
  "ACT-03k": [26, 27, 28, 30]
  "EB-DL-4": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44]
  "EB-DL-5": 2
---

# Isi berkas Download tabel dan ZIP

## Prerequisites
- Aktor: Total Control `Bagas Pratama {runId}` dan Custom `Wulan Anggraini {runId}`.
- Data:
  - DU-070-1: User `Bagas Pratama {runId}`, role Total Control, cakupan seluruh group.
  - DU-070-2: User `Wulan Anggraini {runId}`, role Custom dengan "Manage files": Read pada group `Branch Bandung` beserta descendant.
  - DU-070-3: User `Siti Nur Rahmawati {runId}`, pengunggah seluruh file DU-070-9 sampai DU-070-16 (tampil `Siti N` pada tabel).
  - DU-070-4: Group `Warehouse {runId}` di bawah group `Head Office`, hierarki penuh `Head Office > Warehouse {runId}`.
  - DU-070-5: Group `Warehouse {runId}` di bawah group `Branch Bandung`, hierarki penuh `Branch Bandung > Warehouse {runId}`.
  - DU-070-6: Aset `Laptop Dell Latitude 5420 {runId}`, group DU-070-4, Status `Active`.
  - DU-070-7: Aset `Printer "HP" M404 {runId}`, group DU-070-5, Status `Active`; pada sel CSV tanda kutip di dalam nama digandakan menjadi `""HP""`.
  - DU-070-8: Aset `Scanner Epson DS-530 {runId}`, group DU-070-5, Status `Active`.
  - DU-070-9: File `kontrak, final {runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-070-6, Size `2.0 MB` dari 2097152 byte, aktif.
  - DU-070-10: File `café-élan-{runId}.pdf`, Source `Custom Field Document`, Reference `Warranty Card`, File Format PDF, aset DU-070-6, Size `310.0 KB` dari 317440 byte, aktif.
  - DU-070-11: File `manual-printer-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-070-7, Size `450.0 KB` dari 460800 byte, aktif.
  - DU-070-12: File `scan-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-070-7, Size `300.0 KB` dari 307200 byte, aktif, diunggah lebih dulu daripada DU-070-13.
  - DU-070-13: File `scan-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-070-8, Size `640.0 KB` dari 655360 byte, aktif, diunggah sesudah DU-070-12, nama entri ZIP `scan-{runId} (2).pdf` dari nama kembar DU-070-12.
  - DU-070-14: File `lama-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-070-7, Size `820.4 KB`, berada di Recycle Bin dan masih dalam masa retensi.
  - DU-070-15: File `scan-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-070-7, Size `120.0 KB` dari 122880 byte, aktif, diunggah sesudah DU-070-13, nama entri ZIP `scan-{runId} (3).pdf` dari nama kembar DU-070-12 dan DU-070-13.
  - DU-070-16: File `foto-registrasi-draft-{runId}.jpg`, Source `Asset Photo`, Category `Asset Photo`, File Format JPG, Size `500.0 KB` dari 512000 byte, di-soft-delete saat aset masih Draft sehingga Asset `—`, Group pembuat record Draft `Branch Bandung > Warehouse {runId}`, berada di Recycle Bin dan masih dalam masa retensi.
  - DU-070-17: Aset `Monitor LG 24 {runId}`, group DU-070-4, Status `Unmanaged`, tanpa file.
  - DU-070-18: Aset `Scanner Canon LiDE 400 {runId}`, group DU-070-5, Status `Disposed`, tanpa file.
- Kondisi:
  - Selection Limit bernilai `1000`.
  - Date Format `dd/MM/yy` dan Time Format `HH:mm`.

## Test Steps

### Download CSV: isi per tipe kolom dan escaping
1. `Bagas Pratama {runId}` meminta Download CSV dari tab Asset Documents dengan kata kunci `{runId}` dan urutan File Name A-Z langsung ke server
2. Verifikasi berkas dikirim langsung pada permintaan yang sama tanpa job background dan tanpa notifikasi in-app
3. Verifikasi berkas CSV berenkode UTF-8 dengan BOM
4. Verifikasi baris header memuat kolom File Name, File Format, Source, Reference, Asset, Asset ID, Group, Size, Uploaded By, dan Upload Date
5. Verifikasi berkas memuat enam baris data, yaitu file `café-élan-{runId}.pdf`, `kontrak, final {runId}.pdf`, `manual-printer-{runId}.pdf`, dan tiga file `scan-{runId}.pdf`, tanpa file `lama-{runId}.pdf` yang berada di Recycle Bin
6. Verifikasi urutan baris mengikuti urutan File Name A-Z: `café-élan-{runId}.pdf`, `kontrak, final {runId}.pdf`, `manual-printer-{runId}.pdf`, lalu tiga file `scan-{runId}.pdf`
7. Verifikasi sel File Name `kontrak, final {runId}.pdf` dibungkus tanda kutip ganda karena memuat koma
8. Verifikasi sel Asset `Printer "HP" M404 {runId}` dibungkus tanda kutip ganda dan tanda kutip di dalamnya digandakan menjadi `""HP""`
9. Verifikasi sel File Name `café-élan-{runId}.pdf` terbaca utuh dengan huruf beraksen `é`
10. Verifikasi sel Group untuk file milik aset `Laptop Dell Latitude 5420 {runId}` berisi hierarki penuh dari root `Head Office > Warehouse {runId}`, bukan hanya `Warehouse {runId}`
11. Verifikasi sel Group untuk file milik aset `Printer "HP" M404 {runId}` berisi `Branch Bandung > Warehouse {runId}`, sehingga berbeda dari `Head Office > Warehouse {runId}` walau nama leaf sama
12. Verifikasi sel Uploaded By berisi nama lengkap utuh `Siti Nur Rahmawati {runId}`, bukan format tampilan `Siti N`
13. Verifikasi sel Size berisi nilai numerik asli tanpa satuan dan tanpa pemisah ribuan, bukan teks terformat seperti `2.0 MB`
14. Verifikasi sel Upload Date mengikuti format tanggal dan jam platform `dd/MM/yy HH:mm`

### Download XLSX: sheet dan tipe sel
15. `Bagas Pratama {runId}` meminta Download XLSX dari tab Asset Documents dengan kata kunci `{runId}` dan urutan File Name A-Z langsung ke server
16. Verifikasi berkas XLSX memuat satu sheet bernama `Sheet1`
17. Verifikasi sel Size ditulis sebagai sel angka (number), bukan teks
18. Verifikasi sel Group untuk file milik aset `Laptop Dell Latitude 5420 {runId}` berisi hierarki penuh `Head Office > Warehouse {runId}`
19. Verifikasi berkas XLSX memuat enam baris data yang sama dengan berkas CSV pada langkah 1, dalam urutan yang sama

### Hasil kosong menghasilkan berkas berisi header saja
20. `Bagas Pratama {runId}` meminta Download CSV dari tab Asset Documents dengan kata kunci `tidak-ada-{runId}` langsung ke server
21. Verifikasi berkas CSV hanya memuat baris header kolom yang visible, tanpa baris data

### ZIP Download: nama entri dan file yang disertakan
22. `Wulan Anggraini {runId}` meminta ZIP Download atas file `manual-printer-{runId}.pdf`, file `scan-{runId}.pdf` DU-070-12 dan DU-070-13, file `kontrak, final {runId}.pdf` di luar scope, dan file `lama-{runId}.pdf` di Recycle Bin langsung ke server
23. Verifikasi berkas ZIP bernama `File-Manager-Files.zip`
24. Verifikasi entri ZIP berada dalam satu level tanpa subfolder dan dinamai `[File Name]` apa adanya, termasuk `manual-printer-{runId}.pdf`
25. Verifikasi dua file bernama kembar `scan-{runId}.pdf` masuk sebagai `scan-{runId}.pdf` untuk file DU-070-12 yang diunggah lebih dulu dan `scan-{runId} (2).pdf` untuk file DU-070-13
26. Verifikasi ZIP tidak memuat file `kontrak, final {runId}.pdf` yang berada di luar scope `Wulan Anggraini {runId}`
27. Verifikasi ZIP tidak memuat file `lama-{runId}.pdf` yang berada di Recycle Bin
28. Verifikasi item yang dilewati tidak menimbulkan pesan kegagalan dan ZIP tetap dibuat dengan tiga file yang tersedia
29. `Wulan Anggraini {runId}` meminta ZIP Download atas file `kontrak, final {runId}.pdf` dan file `lama-{runId}.pdf` saja langsung ke server
30. Verifikasi tidak ada berkas ZIP dan permintaan diperlakukan sebagai file tidak tersedia

### Download CSV Recycle Bin: nilai kosong ditulis hyphen
31. `Bagas Pratama {runId}` meminta Download CSV dari Recycle Bin dengan kata kunci `{runId}` dan urutan File Name A-Z langsung ke server
32. Verifikasi berkas bernama `File-Manager-Recycle-Bin`
33. Verifikasi berkas memuat dua baris data, yaitu file `foto-registrasi-draft-{runId}.jpg` lalu file `lama-{runId}.pdf`
34. Verifikasi sel Asset untuk file `foto-registrasi-draft-{runId}.jpg` berisi `-` (hyphen tunggal), bukan sel kosong, bukan `—`, dan bukan teks `null`
35. Verifikasi sel Group untuk file `foto-registrasi-draft-{runId}.jpg` berisi hierarki penuh `Branch Bandung > Warehouse {runId}`

### Download CSV Asset Data: kolom, label badge, dan nilai numerik
36. `Bagas Pratama {runId}` meminta Download CSV dari tab Asset Data dengan kata kunci `{runId}` dan urutan Name A-Z langsung ke server
37. Verifikasi berkas bernama `File-Manager-Asset-Data`
38. Verifikasi baris header tidak memuat kolom Photo
39. Verifikasi berkas memuat dua baris data, yaitu aset `Monitor LG 24 {runId}` lalu aset `Scanner Canon LiDE 400 {runId}`, tanpa aset Active milik spec ini
40. Verifikasi sel Status untuk aset `Monitor LG 24 {runId}` berisi label teks `Unmanaged` dan untuk aset `Scanner Canon LiDE 400 {runId}` berisi label teks `Disposed`
41. Verifikasi sel Group untuk aset `Monitor LG 24 {runId}` berisi hierarki penuh `Head Office > Warehouse {runId}`
42. Verifikasi sel Group untuk aset `Scanner Canon LiDE 400 {runId}` berisi hierarki penuh `Branch Bandung > Warehouse {runId}`
43. Verifikasi sel Files Size untuk aset `Monitor LG 24 {runId}` berisi nilai numerik `0`, bukan teks terformat `0.0 KB`
44. Verifikasi sel Total Size untuk aset `Monitor LG 24 {runId}` ditulis sebagai angka tanpa satuan, bukan teks terformat

### ZIP Download: nama kembar ketiga
45. `Wulan Anggraini {runId}` meminta ZIP Download atas ketiga file `scan-{runId}.pdf` langsung ke server
46. Verifikasi berkas ZIP memuat tiga entri
47. Verifikasi file DU-070-15 yang diunggah paling akhir masuk sebagai `scan-{runId} (3).pdf`
48. Verifikasi penomoran sufiks mengikuti urutan unggah dari yang terlama: `scan-{runId}.pdf` untuk DU-070-12, `scan-{runId} (2).pdf` untuk DU-070-13, dan `scan-{runId} (3).pdf` untuk DU-070-15
