---
id: TC-FA-FASVC-E2E-023-daftar-kosong-lalu-terisi
title: "Daftar Kosong: Empty State, Create Pertama, dan Hapus Record Terakhir"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["S-FASVC-02", "EB-EDG-2"]
smoke: []
dependsOn: []
trace:
  "S-FASVC-02": [1, 2, 3, 18, 19]
  "EB-EDG-2": [12, 13, 14, 18, 19]
anchor: []
coverage:
  web: automated
---

# Daftar Kosong: Empty State, Create Pertama, dan Hapus Record Terakhir

## Prerequisites
- Aktor: Total Control `Wulan Kosong {runId}`, user milik entitas khusus.
- Layar awal: Add-ons > Service Center (halaman daftar).
- Data:
  - Spec ini memakai entitas khusus tanpa satu pun Service Center saat dimulai.
  - DU-023-1: Entitas `Entitas Kosong {runId}`, tidak memuat Service Center apa pun.
  - DU-023-2: User `Wulan Kosong {runId}`, role Total Control, cakupan seluruh Group di `Entitas Kosong {runId}`, Status `Active`.
  - DU-023-3: Group `Cabang Perdana {runId}`, anak langsung dari root pohon Group.
  - DU-023-4: Service Center `Bengkel Perdana {runId}`, Service type `Routine`, Available to `Cabang Perdana {runId}`, City `Kota Perdana {runId}`, Company email `perdana@bengkelperdana.example`; dibuat oleh langkah spec ini dan dihapus kembali oleh spec ini.
- Kondisi: client memiliki lisensi addon Maintenance berstatus aktif.

## Test Steps

### Entitas tanpa Service Center menampilkan empty state daftar kosong
1. Verifikasi empty state dengan judul `No service centers yet` dan keterangan `Get started by creating your first service center.` tampil
2. Verifikasi tombol `[+ Service Center]` pada toolbar daftar tampil
3. Verifikasi empty state tidak memuat tombol

### Create Service Center pertama mengisi daftar yang kosong
4. Klik `[+ Service Center]`
5. Isi Name `Bengkel Perdana {runId}`
6. Centang Service type `Routine`
7. Hilangkan centang `All groups` pada Available to
8. Centang `Cabang Perdana {runId}` pada Available to
9. Isi City `Kota Perdana {runId}`
10. Isi Company email `perdana@bengkelperdana.example`
11. Klik `[Submit]`
12. Verifikasi baris `Bengkel Perdana {runId}` tampil pada daftar
13. Verifikasi laporan paginasi `Showing 1 to 1 of 1` tampil
14. Verifikasi empty state `No service centers yet` tidak tampil

### Hapus Service Center terakhir menampilkan kembali empty state daftar kosong
15. Klik `⋯` pada baris `Bengkel Perdana {runId}`
16. Klik `Delete`
17. Klik `[Delete]` pada dialog `Delete Service Center`
18. Verifikasi empty state dengan judul `No service centers yet` dan keterangan `Get started by creating your first service center.` tampil lagi
19. Verifikasi empty state itu bukan hasil filter kosong: judul `No results found` tidak tampil