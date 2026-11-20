---
id: TC-FA-FASVC-BE-081-be-storage-penuh-lampiran-dan-hapus-berkas-lama
title: "Server: Storage Penuh Menolak Lampiran Baru, Berkas Lama Dihapus dari Penyimpanan Saat Save Dikomit"
layer: be-e2e
priority: High
caseType: Negative
status: draft
owner: BE
sourceRules: ["FASVC-LOGIC-13a", "FASVC-LOGIC-13b", "FASVC-LOGIC-13c", "FASVC-LOGIC-13d", "V-FASVC-40", "EC-FASVC-60", "EC-FASVC-61", "EC-FASVC-62", "EC-FASVC-63", "RX-FASVC-02", "RX-FASVC-33", "RX-FASVC-34", "F-FASVC-07.k4", "F-FASVC-07.k5"]
smoke: []
dependsOn: []
trace:
  "FASVC-LOGIC-13a": [4, 11]
  "FASVC-LOGIC-13b": [17, 19, 21, 24, 27]
  "FASVC-LOGIC-13c": [6, 8, 13, 15]
  "FASVC-LOGIC-13d": [29, 38]
  "V-FASVC-40": [4, 11]
  "EC-FASVC-60": [4, 6, 8, 11, 13]
  "EC-FASVC-61": [17, 19]
  "EC-FASVC-62": [24, 27, 32]
  "EC-FASVC-63": [29, 38]
  "RX-FASVC-02": [29, 36, 38]
  "RX-FASVC-33": [6, 8, 13, 15]
  "RX-FASVC-34": [29, 38]
  "F-FASVC-07.k4": [4, 11]
  "F-FASVC-07.k5": [29, 38]
anchor: []
---

# Server: Storage Penuh Menolak Lampiran Baru, Berkas Lama Dihapus dari Penyimpanan Saat Save Dikomit

## Prerequisites
- Aktor: Total Control `Bagas Penuh {runId}` pada entitas khusus `Klien Storage Penuh BE {runId}`, dan Total Control `Nirina Kuota {runId}` pada entitas khusus `Klien Tanpa Kuota {runId}`.
- Data:
  - DU-081-1: Entitas `Klien Storage Penuh BE {runId}`, Status `Active`, kuota Storage `10.0 GB`, usage ledger Storage `10.0 GB`, tidak dipakai spec lain.
  - DU-081-2: Entitas `Klien Tanpa Kuota {runId}`, Status `Active`, tanpa kuota Storage, usage ledger Storage `12.0 GB`, tidak dipakai spec lain.
  - DU-081-3: User `Bagas Penuh {runId}` dengan Role `Total Control`, cakupan Group seluruh pohon Group pada `Klien Storage Penuh BE {runId}`.
  - DU-081-4: User `Nirina Kuota {runId}` dengan Role `Total Control`, cakupan Group seluruh pohon Group pada `Klien Tanpa Kuota {runId}`.
  - DU-081-5: Service Center `Servis Edit Penuh {runId}` pada `Klien Storage Penuh BE {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, Company email `kontak@penuh081.co.id`, Status `Active`, dengan satu lampiran `izin-lama-081.pdf` (PDF, 300 KB).
  - DU-081-6: Service Center `Servis Ganti Tanpa Kuota {runId}` pada `Klien Tanpa Kuota {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company email `kontak@tanpakuota081.co.id`, Status `Active`, dengan satu lampiran `izin-nk-081.pdf` (PDF, 300 KB).
  - Setiap Create yang dikirim memuat field wajib lain bernilai Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, dan Company email `info@penuh081.co.id`, kecuali yang disebut di langkah; Name dikirim sesuai langkah.
  - Setiap Edit yang dikirim memuat versi data terkini dan nilai tersimpan untuk semua field selain yang disebut di langkah.
- Kondisi:
  - Storage `Klien Storage Penuh BE {runId}` penuh sepanjang spec: Used Storage `10.0 GB` dan Storage Quota `10.0 GB`.
  - Lisensi addon Maintenance aktif pada kedua entitas.

## Test Steps

### Create dengan berkas baru ditolak saat Storage penuh dan tidak menyimpan apa pun
1. `Bagas Penuh {runId}` membaca daftar Service Center dengan pencarian `Sentral Penuh Baru {runId}` dan mencatat jumlah barisnya sebagai N0
2. Catat jumlah entri Changelog dengan Service Center Name `Sentral Penuh Baru {runId}` sebagai L0, jumlah entri Activity Log dengan Object `Service Center` dan Name `Sentral Penuh Baru {runId}` sebagai A0, dan jumlah entri System Log Detail User `Bagas Penuh {runId}` dengan Action `Created` sebagai S0
3. `Bagas Penuh {runId}` mengirim Create dengan Name `Sentral Penuh Baru {runId}` dan lampiran `brosur-penuh-081.pdf` (PDF, 500 KB)
4. Verifikasi permintaan ditolak karena Storage penuh
5. Baca ulang daftar Service Center dengan pencarian `Sentral Penuh Baru {runId}`
6. Verifikasi jumlah baris tetap N0, sehingga Service Center tidak dibuat
7. Baca ulang Changelog dengan Service Center Name `Sentral Penuh Baru {runId}`, Activity Log dengan Object `Service Center` dan Name `Sentral Penuh Baru {runId}`, dan System Log Detail User `Bagas Penuh {runId}`
8. Verifikasi jumlah entri Changelog tetap L0, Activity Log tetap A0, dan System Log Action `Created` tetap S0

### Edit yang mengganti lampiran ditolak saat Storage penuh dan berkas lama tetap
9. Catat alamat lampiran `izin-lama-081.pdf` milik `Servis Edit Penuh {runId}`
10. `Bagas Penuh {runId}` mengirim Edit atas `Servis Edit Penuh {runId}` dengan lampiran `izin-lama-081.pdf` diganti `izin-baru-081.pdf` (PDF, 400 KB)
11. Verifikasi permintaan ditolak karena Storage penuh
12. Baca `Servis Edit Penuh {runId}` dari daftar dengan pencarian `Servis Edit Penuh {runId}`
13. Verifikasi Service Center tetap memiliki tepat satu lampiran yang berasal dari berkas `izin-lama-081.pdf`
14. Ambil berkas dari alamat lampiran yang dicatat pada langkah 9
15. Verifikasi berkas masih dapat diambil, karena Save yang ditolak tidak menghapus berkas lama

### Format dan ukuran didahulukan sebelum Storage penuh
16. `Bagas Penuh {runId}` mengirim Create dengan Name `Sentral Penuh Format {runId}` dan lampiran `kontrak-servis-081.docx` (DOCX, 200 KB)
17. Verifikasi permintaan ditolak dengan pesan `Select a PDF, JPG, or PNG file.`
18. `Bagas Penuh {runId}` mengirim Create dengan Name `Sentral Penuh Ukuran {runId}` dan lampiran `katalog-besar-081.pdf` (PDF, 11 MB)
19. Verifikasi permintaan ditolak dengan pesan `File size must not exceed 1 MB.`
20. `Bagas Penuh {runId}` mengirim Create dengan Name `Sentral Penuh Dua Berkas {runId}` dan dua lampiran `izin-baru-081.pdf` (PDF, 400 KB) dan `sertifikat-081.pdf` (PDF, 400 KB)
21. Verifikasi permintaan ditolak dengan pesan `Up to 1 file.`

### Create dan Edit tanpa lampiran baru tidak diblokir saat Storage penuh
22. `Bagas Penuh {runId}` mengirim Create dengan Name `Sentral Penuh Tanpa Lampiran {runId}` tanpa lampiran
23. Baca `Sentral Penuh Tanpa Lampiran {runId}` dari daftar dengan pencarian `Sentral Penuh Tanpa Lampiran {runId}`
24. Verifikasi Service Center tersimpan tanpa lampiran
25. `Bagas Penuh {runId}` mengirim Edit atas `Servis Edit Penuh {runId}` dengan lampiran `izin-lama-081.pdf` dihapus
26. Baca `Servis Edit Penuh {runId}` dari daftar dengan pencarian `Servis Edit Penuh {runId}`
27. Verifikasi Service Center tersimpan tanpa lampiran, sehingga Edit yang hanya menghapus lampiran tidak diblokir
28. Ambil berkas dari alamat lampiran yang dicatat pada langkah 9
29. Verifikasi berkas tidak ditemukan, karena berkas lama dihapus dari penyimpanan dalam transaksi Save yang sama

### Client tanpa kuota Storage tidak diblokir dan penggantian lampiran menghapus berkas lama
30. `Nirina Kuota {runId}` mengirim Create dengan Name `Sentral Tanpa Kuota Baru {runId}` dan lampiran `brosur-nk-081.pdf` (PDF, 500 KB)
31. Baca `Sentral Tanpa Kuota Baru {runId}` dari daftar dengan pencarian `Sentral Tanpa Kuota Baru {runId}`
32. Verifikasi Service Center memiliki tepat satu lampiran yang berasal dari berkas `brosur-nk-081.pdf`, sehingga client tanpa kuota Storage tidak diblokir
33. Catat alamat lampiran `izin-nk-081.pdf` milik `Servis Ganti Tanpa Kuota {runId}`
34. `Nirina Kuota {runId}` mengirim Edit atas `Servis Ganti Tanpa Kuota {runId}` dengan lampiran `izin-nk-081.pdf` diganti `izin-nk-baru-081.pdf` (PDF, 400 KB)
35. Baca `Servis Ganti Tanpa Kuota {runId}` dari daftar dengan pencarian `Servis Ganti Tanpa Kuota {runId}`
36. Verifikasi Service Center memiliki tepat satu lampiran yang berasal dari berkas `izin-nk-baru-081.pdf`
37. Ambil berkas dari alamat lampiran yang dicatat pada langkah 33
38. Verifikasi berkas tidak ditemukan, karena berkas lama dihapus dari penyimpanan dalam transaksi Save yang sama
