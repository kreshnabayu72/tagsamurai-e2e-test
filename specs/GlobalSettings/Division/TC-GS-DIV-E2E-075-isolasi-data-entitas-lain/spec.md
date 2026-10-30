---
id: TC-GS-DIV-E2E-075-isolasi-data-entitas-lain
title: "Isolasi Data: Division Entitas Lain Tidak Terlihat"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-266
coverage:
  web: automated
---

# Isolasi Data: Division Entitas Lain Tidak Terlihat

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji:

  | Peran dalam spec | Role | Email | Environment variable password |
  |---|---|---|---|
  | Aktor UI dan pemilik token pada request daftar (entitas A) | Total Control Client A (Sari Dewi) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |
  | Pemilik data entitas B (hanya lewat API, tanpa login UI) | Total Control Client B (Lina Kusuma) | `totalControl_automated_qaTeam2@qwertysystem.net` | `GS_CLIENTB_TC_PASSWORD` |

  Login aktor UI (entitas A) di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Akun Client B tidak tercantum di Tabel Data Uji Pre-setup Division; akun ini mengikuti suite Brand dan disediakan tim FE. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`, `GS_CLIENTB_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup entitas A (tetap di environment, tidak diubah, tanpa suffix `{runId}`): `Finance` (FIN) sebagai anchor bahwa data entitas A tampil.
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), di-seed lewat API (kemampuan seeding Division lewat API) di hook `before`:
  - `Isolasi Unit B {runId}-075` di entitas B (Division milik entitas B yang tidak ada di entitas A; dibuat dengan sesi akun Client B).
  - `Isolasi Unit A {runId}-075` di entitas A, sebagai anchor bahwa entri milik entitas A tampil di Changelog.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Isolasi Unit B {runId}-075` di entitas B (sesi akun Client B) dan `Isolasi Unit A {runId}-075` di entitas A.
- Kemampuan teknis: klien HTTP yang mengirim request daftar Division langsung ke server dengan token sesi akun entitas A, tanpa lewat UI (endpoint dan cara menangkap token disediakan tim FE).
- Tidak ada state global yang diubah.
- TC-GS-DIV-266: login sebagai Total Control entitas A dan berada di Global Settings > User > Division.

## Test Steps

### TC-GS-DIV-266: Data Division entitas lain tidak terlihat

1. Buka Tab Division
2. Ketik Search `Finance`, tekan Enter pada tabel Division
3. Verifikasi hanya Division milik entitas A yang tampil di tabel (`Finance` tampil)
4. Ganti isi kotak search dengan `Isolasi Unit B {runId}-075`, tekan Enter
5. Verifikasi Division milik entitas B `Isolasi Unit B {runId}-075` tidak ada di tabel
6. Klik `(←)` pada kotak Search
7. Klik icon `[Changelog]` pada toolbar
8. Ketik Search `Isolasi Unit A {runId}-075`, tekan Enter pada Modal Changelog
9. Verifikasi entri milik entitas A `Isolasi Unit A {runId}-075` tampil di Changelog
10. Ganti isi kotak search Modal Changelog dengan `Isolasi Unit B {runId}-075`, tekan Enter
11. Verifikasi entri `Isolasi Unit B {runId}-075` tidak ada di Changelog
12. Tutup Modal Changelog lewat `✕`
13. Kirim request daftar Division dengan token sesi entitas A langsung ke server
14. Verifikasi hasil request memuat Division milik entitas A `Finance`
15. Verifikasi hasil request tidak memuat Division milik entitas B `Isolasi Unit B {runId}-075`

## Notes

- Sumber: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE. Kelas multi-konteks (prinsip 13c), jenis dua tenant. Spec berjalan dengan satu sesi UI (entitas A); data entitas B hanya di-seed dan dibersihkan lewat API.
- Langkah 2 sampai 3 dan 8 sampai 9 (anchor positif): asersi absence pada tabel dan Changelog didahului bukti bahwa entri milik entitas A tampil di surface yang sama (bagian 8b butir 2).
- Langkah 4 menjalankan "Bandingkan dengan Division milik entitas B" (langkah 2 TC) sebagai pencarian nama Division entitas B di tabel entitas A.
- Request langsung ke server (langkah 13): asersi hanya isi respons (bagian 8b butir 1).
- Langkah 1 adalah Langkah Uji 1 TC-GS-DIV-266 ("buka Tab Division"), sehingga dipertahankan (konvensi bagian 4).
- Langkah penghubung: langkah 2, 4, 8, dan 10 (Search nama yang diasersi); langkah 6 (mengosongkan Search); langkah 12 (menutup Modal Changelog).
- Langkah 3 adalah `Verifikasi` Expected Result a TC ("Hanya Division milik entitas A yang tampil"); `Finance` yang tampil pada langkah 3 sekaligus menjadi anchor positif bagi asersi absence langkah 5, dan langkah 5 melengkapi Expected Result a dari sisi entitas B. Asersi tambahan: langkah 9 dan 14 adalah anchor positif dari Division milik entitas A.
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-DIV-266: TC tidak menyebut nama Division milik entitas B maupun cara menyiapkannya (precondition hanya "Entitas B memiliki Division yang tidak ada di entitas A"); spec memakai `Isolasi Unit B {runId}-075` yang di-seed lewat API dengan sesi akun Client B, yang disediakan tim FE.
  - TC-GS-DIV-266: Post Condition `Data Division tidak berubah` tidak punya langkah observasi atau Expected padanan sehingga tidak diasersi.
  - TC-GS-DIV-266: anchor Changelog (langkah 8 sampai 9) mengasumsikan seeding Division lewat API menulis entri Changelog; bila seeding tidak mencatat Changelog, anchor itu perlu diganti dengan aksi Create lewat UI.
  - TC-GS-DIV-266: akun Client B (`totalControl_automated_qaTeam2@qwertysystem.net`, `GS_CLIENTB_TC_PASSWORD`) mengikuti suite Brand dan tidak ada di Tabel Data Uji Pre-setup Division.
