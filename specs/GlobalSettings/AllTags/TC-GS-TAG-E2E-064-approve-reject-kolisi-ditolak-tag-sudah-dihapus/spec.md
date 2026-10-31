---
id: TC-GS-TAG-E2E-064-approve-reject-kolisi-ditolak-tag-sudah-dihapus
title: "Approve/Reject Kolisi Ditolak saat Tag Sudah Dihapus tetapi Event Delete Belum Diproses"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-TAG-352
coverage:
  web: automated
---

# Approve/Reject Kolisi Ditolak saat Tag Sudah Dihapus tetapi Event Delete Belum Diproses

## Prerequisites

- Mode: FE+BE (backend nyata; kelas d, event/background job: konsumen event Delete TAG ditahan lalu dilepas). Spec ini menghapus tag DD-03 lewat pemicu API.
- Akun aktor: Principal approver (Mira Anggraini) `principalApprover_automated@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`. Login di hook `before` (sesi Admin Console); hook `after` mengembalikan sesi ke akun default suite. Kesamaan akun ini dengan env var terdaftar perlu dikonfirmasi tim FE saat tahap script (Q-2, kategori B).
- Pemicu (penahanan konsumen event lewat fixture BE; penghapusan lewat sesi API aktor, tidak diasersi): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`, menghapus tag DD-03 dari registri Global Settings sementara konsumen event Delete TAG ditahan (precondition TC: "lewat sesi lain").
- Layar awal: hook `beforeEach` membuka Admin Console > Approvals > TAG Stock Tab Active.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30), dengan DD-03 `04A224B2C15E80` (NFC Waiting for Approval) dan subject `Activation Collision` DD-03 berstatus `pending` di Tab Active Approvals > TAG Stock. Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); fixture BE memulihkan kondisi awal sebelum spec.
- Sesi API aktor (kemampuan dinyatakan di `suite.md`): Total Control Client A menghapus DD-03 (langkah 3).
- Kemampuan teknis (disediakan tim FE/BE): penahanan dan pelepasan konsumen event Delete TAG lewat fixture BE (Q-5; mekanisme tidak didefinisikan di TC, PRD, atau LLD); sesi API Total Control Client A yang menghapus DD-03; penanda event Delete selesai diproses (Eventual); pembacaan TAG Code yang diterbitkan untuk subject (untuk Expected b); seed dan reset idempotent Seed Registri A dan subject Approvals. Langkah dan selektor Approvals tidak didefinisikan di TC, PRD, atau LLD (Q-9).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): lepas konsumen event Delete TAG yang masih ditahan, kembalikan Seed Registri A (DD-03) dan subject Approvals lewat fixture BE; sesi dikembalikan ke akun default suite.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain data di atas dan sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-352: Submit Approve ditolak saat tag sudah dihapus

1. Buka Detail Approval subject `Activation Collision` DD-03 `04A224B2C15E80` dari Tab Active
2. Pilih radio Approve
3. Hapus tag DD-03 dari registri Global Settings lewat sesi API Total Control Client A sementara konsumen event Delete TAG ditahan, hingga tersimpan
4. Klik `Submit` pada Detail Approval
5. Verifikasi dialog nested berjudul `Approval cannot be made` dengan isi `This request has already been resolved.` dan satu tombol `Close`
6. Klik `Close` pada dialog nested
7. Verifikasi dialog nested dan Detail Approval tertutup sekaligus
8. Verifikasi Tab Active di-refresh
9. Verifikasi tidak ada TAG Code yang diterbitkan untuk subject DD-03
10. Lepas tahan konsumen event Delete TAG
11. Tunggu event Delete diproses (Eventual)
12. Klik Tab History
13. Verifikasi subject DD-03 tampil di Tab History dengan Approval `Canceled`
14. Verifikasi Approver subject DD-03 `—`

## Notes

- Mode: FE+BE. Kelas d (event/background). Spec memuat satu TC.
- Langkah 3 (penghapusan DD-03 lewat sesi API Total Control Client A dengan konsumen event ditahan) hanyalah pemicu state; objek asersi adalah dialog dan Tab History di Approvals.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1 dan 2 (membuka Detail Approval dengan radio Approve terpilih sebagai precondition TC).
- Asersi tambahan di luar Expected TC (S-03): tidak ada.
- Temuan untuk QA:
  - Judul/skenario TC menyebut "Approve/Reject", tetapi langkah TC hanya menjalankan Approve (radio Approve terpilih); varian Reject tidak punya langkah di TC.
  - Q-5: pemicu "konsumen event Delete TAG ditahan" tidak deterministik dan mekanismenya tidak didefinisikan di TC; disediakan tim BE.
  - Q-9: langkah dan selektor Approvals (Detail Approval, radio Approve, Tab Active/History) tidak didefinisikan.
  - Q-2: Pre-setup TC memakai `principalApprover_automated`, sedangkan `.env.example` mendaftarkan `totalControlPrincipal_automated_qaTeam1` (GS_PRINCIPAL_TC); kesamaan perlu dikonfirmasi tim FE saat tahap script (Q-2, kategori B). Precondition c TC menyebut "Total Control (Client A) sudah menghapus tag ... lewat sesi lain" tanpa menyebut akun pelaku.
  - TC-GS-TAG-352 Expected b "tidak ada TAG Code diterbitkan" tidak menyebut cara mengamati; spec memakai pembacaan lewat fixture BE (disediakan tim FE/BE).
  - Post Condition butir a ("Subject tidak berubah oleh `Submit` ini") sejalan dengan Expected c; butir b ("Tidak ada entri Approved/Rejected di Changelog") tidak punya langkah observasi di TC dan tidak diasersi.
  - Q-4: identifier DD-03 tetap; kondisi subject pending dipulihkan lewat fixture BE sebelum spec.
