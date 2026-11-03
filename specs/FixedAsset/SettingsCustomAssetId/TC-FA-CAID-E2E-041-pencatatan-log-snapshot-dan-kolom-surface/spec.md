---
id: TC-FA-CAID-E2E-041-pencatatan-log-snapshot-dan-kolom-surface
title: "Pencatatan Log: Snapshot Immutable, Kolom Object dan Name, serta Opsi Filter Object"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-248
  - TC-FA-CAID-249
  - TC-FA-CAID-250
coverage:
  web: automated
---

# Pencatatan Log: Snapshot Immutable, Kolom Object dan Name, serta Opsi Filter Object

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson, Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup: Company Alpha dengan baseline B1 (No 10); baseline B1 disiapkan ulang lewat seed API pada langkah pertama TC-FA-CAID-249 dan TC-FA-CAID-250. General Settings Date Format `dd/MM/yy` dan Time Format 24 jam (No 27): dipakai sebagai precondition TC, tidak diasersi.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md); kemampuan membaca jumlah entri Object `Custom Asset ID` di Modal Changelog: Custom Asset ID, System Log (Detail User), dan Activity Log (tab User Action) sebelum aksi (disediakan tim FE/BE; audit trail permanen sehingga jumlah entri diasersi sebagai selisih terhadap baseline, S-12).
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: Separator konfigurasi Company Alpha berubah di tiap TC. Hook `after` suite memulihkan Company Alpha ke baseline B1 dan aset A1 sampai A5. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-248: Entri log lama tidak berubah (snapshot immutable)

1. Catat baseline jumlah entri Object `Custom Asset ID` pada Modal Changelog: Custom Asset ID
2. Pilih Separator `- (Dash)`, lalu klik `[Save]`
3. Pilih Separator `. (Dot)`, lalu klik `[Save]`
4. Tunggu aksi selesai: tombol `[Save]` kembali disabled
5. Buka Modal Changelog: Custom Asset ID
6. Verifikasi Changelog bertambah dua entri Separator terpisah dibanding baseline: `Slash` ke `Dash` (lama) dan `Dash` ke `Dot` (baru)
7. Verifikasi entri lama tetap `Slash` ke `Dash` dan tidak ter-overwrite
8. Tutup Modal Changelog: Custom Asset ID

### TC-FA-CAID-249: Kolom Object dan Name pada System Log dan Activity Log

9. Atur konfigurasi Company Alpha ke baseline B1 (seed API), buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada System Log dan Activity Log
10. Pilih Separator `- (Dash)`, lalu klik `[Save]`
11. Tunggu aksi selesai: tombol `[Save]` kembali disabled
12. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
13. Verifikasi entri baru dibanding baseline menampilkan Object `Custom Asset ID` dan Name `—`
14. Verifikasi System Log tidak memiliki kolom Modified By
15. Buka Fixed Asset > Activity Log > tab User Action
16. Verifikasi entri baru dibanding baseline menampilkan Object `Custom Asset ID` dan Name `—`
17. Verifikasi entri baru Activity Log menampilkan Modified By `Sarah J`

### TC-FA-CAID-250: Opsi filter Object Activity Log

18. Atur konfigurasi Company Alpha ke baseline B1 (seed API), lalu buka Fixed Asset > Settings > Asset Master > Custom Asset ID
19. Pilih Separator `- (Dash)`, lalu klik `[Save]`
20. Tunggu aksi selesai: tombol `[Save]` kembali disabled
21. Buka Fixed Asset > Activity Log > tab User Action dan klik icon Filter
22. Buka dropdown `Object`
23. Verifikasi opsi `Custom Asset ID` tersedia sebagai nilai Object yang tercatat

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 1 dan 9 (baseline jumlah entri, S-12), langkah 8 (menutup modal), langkah 9 dan 18 (seed baseline B1 dan membuka tab), langkah 4, 11, dan 20 (tunggu aksi selesai sebelum membuka surface log, bagian 8b butir 8), serta membuka System Log dan Activity Log.
- Dua Save berurutan pada langkah 2 dan 3 mengikuti dua aksi Save pada TC-FA-CAID-248; Save kedua dikirim pada halaman yang sama tanpa berpindah surface sehingga tidak ada langkah tunggu di antaranya, dan langkah 4 menunggu Save kedua selesai sebelum Modal Changelog dibuka.
- Pembagian TC lintas spec: TC-FA-CAID-233 sampai 235 ada di spec 037, TC-FA-CAID-236 sampai 238 di spec 038, TC-FA-CAID-239 sampai 242 di spec 039, TC-FA-CAID-243 sampai 245 di spec 040.
- Temuan untuk QA:
  - TC-FA-CAID-248 tidak menyebut cara mengidentifikasi dua entri Separator di tengah audit trail permanen; spec memakai baseline jumlah entri dan mengidentifikasi dua entri lewat nilai Old/New.
  - TC-FA-CAID-250 menyebut opsi Object "yang tercatat" tanpa menyebut daftar opsi lain; spec hanya mengasersi keberadaan opsi `Custom Asset ID` (G-6 pada catatan TC).
  - Post Condition TC-FA-CAID-248 sampai 250 tidak diasersi karena TC tidak memberi langkah observasinya.
