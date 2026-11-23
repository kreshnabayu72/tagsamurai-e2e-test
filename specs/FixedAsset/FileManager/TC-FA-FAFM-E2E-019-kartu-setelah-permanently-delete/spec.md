---
id: TC-FA-FAFM-E2E-019-kartu-setelah-permanently-delete
title: "Kartu Storage Usage dan tab Asset Data sesudah Permanently Delete"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [SYN-02a, SYN-02b, SYN-02c, SYN-02d, SYN-02f, SYN-02h, SYN-02i]
smoke: []
dependsOn: []
trace:
  SYN-02a: 12
  SYN-02b: 12
  SYN-02c: 15
  SYN-02d: 19
  SYN-02f: [15, 19, 22]
  SYN-02h: 16
  SYN-02i: 19
anchor: [2, 3, 6, 9]
coverage:
  web: automated
---

# Kartu Storage Usage dan tab Asset Data sesudah Permanently Delete

## Prerequisites
- Aktor: Total Control.
- Layar awal: Halaman utama Fixed Asset.
- Data:
  - DU-019-1: Entitas khusus `FAMS Kartu Permanen {runId}`.
  - DU-019-2: Aset `Laptop Dell Latitude 5420 {runId}` berstatus Active, Group `Head Office`, dengan file aktif `laptop-front-{runId}.jpg`, Source `Asset Photo`, Kategori `Asset Photo`, Size `300.0 KB`.
  - DU-019-3: Aset `Printer HP LaserJet {runId}` berstatus `Disposed`, Group `Head Office`.
  - DU-019-4: File di Recycle Bin `disposal-old-{runId}.pdf`, Source `Disposal Document`, Size `150.0 KB`, Deleted By `System`, Asset `Printer HP LaserJet {runId}`, Group `Head Office`, yang dihapus permanen pada spec ini.
  - Files Size aset `Printer HP LaserJet {runId}` pada tab `Disposed & Unmanaged Assets` yang diharapkan `150.0 KB` sebelum dan `0.0 KB` sesudah DU-019-4 dihapus permanen.
  - Fixed Asset yang diharapkan sesudah DU-019-4 dihapus permanen: lebih kecil `150.0 KB` dari nilai sebelum aksi pada langkah 3.
- Kondisi:
  - Spec ini memakai entitas khusus DU-019-1 yang tidak dipakai spec lain.
  - Data & Log Size aset `Disposed` dibentuk server dan nilainya tidak ditetapkan spec, sehingga Fixed Asset dan Total Size dibandingkan dengan selisih, bukan dengan nilai mutlak.
  - Total Used pada kartu berasal dari Global Settings > File Manager dan dilaporkan berkala sebagai snapshot, sehingga dapat tertinggal dari Fixed Asset sampai laporan berkala berikutnya. Pemakaian entitas ini hanya berasal dari FAMS, sehingga sesudah laporan berkala berjalan `Total Used` sama dengan `Fixed Asset`.

## Test Steps

### Kartu, label tab, dan tab Asset Data sebelum Permanently Delete
1. Buka File Manager lewat grup `Settings` di sidebar Fixed Asset
2. Verifikasi label tab `Asset Photo (300.0 KB)` sebelum Permanently Delete
3. Verifikasi kartu `Storage Usage` menampilkan nilai `Fixed Asset` terisi, dicatat sebagai nilai awal
4. Klik tab `Disposed & Unmanaged Assets`
5. Ketik Search `{runId}`, tekan Enter
6. Verifikasi aset `Printer HP LaserJet {runId}` tampil dengan Files Size `150.0 KB`

### Permanently Delete satu file dari Recycle Bin
7. Klik tombol `Recycle Bin` pada header kartu `Storage Usage`
8. Ketik Search `{runId}`, tekan Enter
9. Verifikasi file `disposal-old-{runId}.pdf` tampil di Recycle Bin
10. Klik `Permanently Delete` pada baris `disposal-old-{runId}.pdf`
11. Klik `[Permanently Delete]` pada dialog `Permanently Delete File`
12. Verifikasi file `disposal-old-{runId}.pdf` tidak tampil lagi di Recycle Bin
13. Tutup modal `Recycle Bin`

### Kartu, label tab, dan tab Asset Data sesudah dibaca ulang
14. Muat ulang halaman
15. Verifikasi kartu `Fixed Asset` lebih kecil 150.0 KB dari nilai awal pada langkah 3
16. Verifikasi label tab `Asset Photo (300.0 KB)` tidak berubah sesudah Permanently Delete
17. Klik tab `Disposed & Unmanaged Assets`
18. Ketik Search `{runId}`, tekan Enter
19. Verifikasi aset `Printer HP LaserJet {runId}` tampil dengan Files Size `0.0 KB`

### Total Used menyamai Fixed Asset sesudah laporan berkala
20. Laporan berkala pemakaian FAMS berjalan
21. Muat ulang halaman
22. Verifikasi `Total Used` pada kartu `Storage Usage` sama dengan nilai `Fixed Asset` pada kartu
